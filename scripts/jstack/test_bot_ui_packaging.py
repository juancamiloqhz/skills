"""Exercise an installed-style package without the source checkout on sys.path."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[2] / 'skills/jstack/jstack-make-bot-ui'


class InstalledBotUITest(unittest.TestCase):
    def test_copied_package_serves_assets_and_retains_a_request_for_receiver_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            package = root / 'installed skill'
            shutil.copytree(PACKAGE, package)
            script = r'''
import http.client, json, sys, threading
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]) / 'scripts'))
from bot_ui_local import Journal, make_server
from bot_ui_transport import Receipt
journal = Journal(Path(sys.argv[2]) / 'requests.sqlite', 'example/fixture', 123)
calls = []
def send(payload):
    calls.append(payload)
    return Receipt(payload['requestId'], 'accepted', 202, 'delivery:fixture')
server = make_server(('127.0.0.1', 0), ['http://fixture.local'], journal, send)
thread = threading.Thread(target=server.serve_forever)
thread.start()
try:
    for path, expected in [('/', b'Check PR'), ('/app.js', b'./requests'), ('/scope', b'example/fixture')]:
        c = http.client.HTTPConnection(*server.server_address, timeout=5)
        c.request('GET', path, headers={'Host':'fixture.local'})
        response = c.getresponse()
        assert response.status == 200 and expected in response.read(), path
        c.close()
    for _ in range(2):
        c = http.client.HTTPConnection(*server.server_address, timeout=5)
        c.request('POST', '/requests', json.dumps({'requestId':'isolated-click'}),
                  {'Host':'fixture.local','Origin':'http://fixture.local','Content-Type':'application/json'})
        response = c.getresponse()
        assert response.status == 200
        assert json.loads(response.read())['delivery']['outcome'] == 'accepted'
        c.close()
    assert len(calls) == 1
finally:
    server.shutdown()
    server.server_close()
    thread.join()
'''
            result = subprocess.run([sys.executable, '-I', '-B', '-c', script, str(package), str(root)],
                                    cwd=root, capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
            command = [sys.executable, '-E', '-B', str(package / 'scripts/bot_ui_local.py'),
                       '--journal', str(root / 'requests.sqlite'), '--repository', 'example/fixture',
                       '--pr', '123', 'pending']
            result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            pending = json.loads(result.stdout)
            self.assertEqual(len(pending), 1)
            self.assertEqual(pending[0]['payload']['requestId'], 'isolated-click')
            self.assertIsNone(pending[0]['owner'])


if __name__ == '__main__':
    unittest.main()
