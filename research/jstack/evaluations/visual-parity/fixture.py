"""Generate a small visual migration workspace and serve it on a free port."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import sys

CSS = '''body { margin: 0; background: white; }
.tile { position: absolute; left: 40px; top: 40px; width: 80px; height: 60px; }
.card { background: #3464a4; border: 2px solid #102030; }
.badge { background: #3464a4; border: 2px solid #102030; border-radius: 8px; }
.active { box-shadow: 0 0 0 3px #a04020; }
'''
ROOT = Path(sys.argv[1]).resolve()
if '--prepare' in sys.argv:
    ROOT.mkdir(parents=True, exist_ok=False)
    (ROOT / 'original.css').write_text(CSS)
    # Candidate starts only after the coordinator freezes baseline captures.
    print(ROOT)
    raise SystemExit


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        component = q.get('component', ['card'])[0]
        state = q.get('state', ['idle'])[0]
        version = q.get('version', ['original'])[0]
        if component not in ('card', 'badge') or state not in ('idle', 'active') or version not in ('original', 'candidate'):
            self.send_error(400)
            return
        css = (ROOT / (version + '.css')).read_text()
        body = ('<!doctype html><meta charset="utf-8"><title>Tile gallery</title>'
                '<style>' + css + '</style><main aria-label="Tile gallery">'
                f'<div class="tile {component} {state}" aria-label="{component} {state}"></div></main>').encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 0), Handler)
    print(json.dumps({'port': server.server_port}), flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
