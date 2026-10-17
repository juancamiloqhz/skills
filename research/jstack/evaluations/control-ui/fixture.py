"""Serve a disposable UI without installing browser or project dependencies."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PAGE = b'''<!doctype html><html lang="en"><meta charset="utf-8">
<title>Parcel desk</title><style>
body { font: 20px sans-serif; margin: 40px; }
button, input { font: inherit; margin: 8px; }
</style><main data-app="parcel-desk"><h1>Parcel desk</h1>
<label>Recipient <input id="recipient"></label><section id="actions">
<button id="add">Add parcel</button></section><p role="status">0 parcels</p>
<script>
let count = 0;
function connect() {
  document.querySelector('#add').onclick = () => {
    count++;
    document.querySelector('[role="status"]').textContent =
      count + ' parcels for ' + document.querySelector('#recipient').value;
    document.querySelector('#actions').innerHTML = '<button id="add">Add parcel</button>';
    connect();
  };
}
connect();
</script></main></html>'''
DECOY = b'<!doctype html><title>Parcel archive</title><h1>Parcel archive</h1><button>Export</button>'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        page = DECOY if self.path == '/archive' else PAGE
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 0), Handler)
    print(json.dumps({'port': server.server_port}), flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
