#!/usr/bin/env python3
"""Local evaluation API: listening precedes migration and optional demo seed."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import sqlite3
import threading
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, required=True)
    parser.add_argument('--instance-file', type=Path, required=True)
    parser.add_argument('--delay', type=float, default=2)
    parser.add_argument('--skip-seed', action='store_true')
    args = parser.parse_args()
    args.data_dir.mkdir(parents=True, exist_ok=True)
    database = args.data_dir / 'app.sqlite'
    ready = threading.Event()

    def initialize():
        time.sleep(args.delay)
        with sqlite3.connect(database) as db:
            db.executescript('CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY);'
                             'CREATE TABLE IF NOT EXISTS runs (id INTEGER PRIMARY KEY, project TEXT, name TEXT);')
            if not args.skip_seed:
                db.execute('INSERT OR IGNORE INTO projects VALUES (?)', ('demo',))
        ready.set()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def send_json(self, status, body):
            payload = json.dumps(body).encode()
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            if self.path == '/health':
                self.send_json(200, {'app': 'seed-demo', 'version': 1, 'pid': os.getpid()})
                return
            if not ready.is_set():
                self.send_json(503, {'error': 'initializing'})
                return
            if self.path == '/ready':
                self.send_json(200, {'initialized': True})
            elif self.path == '/projects':
                with sqlite3.connect(database) as db:
                    projects = [row[0] for row in db.execute('SELECT id FROM projects ORDER BY id')]
                self.send_json(200, {'projects': projects})
            elif self.path == '/projects/demo/runs':
                with sqlite3.connect(database) as db:
                    runs = [{'id': row[0], 'name': row[1]} for row in db.execute(
                        'SELECT id, name FROM runs WHERE project = ? ORDER BY id', ('demo',))]
                self.send_json(200, {'runs': runs})
            else:
                self.send_json(404, {'error': 'not found'})

        def do_POST(self):
            if not ready.is_set():
                self.send_json(503, {'error': 'initializing'})
                return
            if self.path != '/projects/demo/runs':
                self.send_json(404, {'error': 'not found'})
                return
            try:
                body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', '0'))))
                if not isinstance(body, dict) or not isinstance(body.get('name'), str) or not body['name']:
                    raise ValueError('name required')
            except (ValueError, TypeError):
                self.send_json(400, {'error': 'name required'})
                return
            with sqlite3.connect(database) as db:
                if db.execute('SELECT id FROM projects WHERE id = ?', ('demo',)).fetchone() is None:
                    self.send_json(409, {'error': 'demo project seed missing'})
                    return
                result = db.execute('INSERT INTO runs (project, name) VALUES (?, ?)', ('demo', body['name']))
                run_id = result.lastrowid
            self.send_json(201, {'id': run_id, 'project': 'demo', 'name': body['name']})

    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    args.instance_file.parent.mkdir(parents=True, exist_ok=True)
    args.instance_file.write_text(json.dumps({'app': 'seed-demo', 'version': 1, 'pid': os.getpid(),
                                            'port': server.server_port, 'dataDir': str(args.data_dir.resolve())}))
    threading.Thread(target=initialize, daemon=True).start()
    try:
        server.serve_forever()
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
