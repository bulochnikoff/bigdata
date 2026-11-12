import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

CHECKPOINT = os.environ.get("CHECKPOINT_PATH", "/data/checkpoint.json")

def load_state():
    if not os.path.exists(CHECKPOINT):
        return {"served": 0}
    with open(CHECKPOINT, encoding="utf-8") as src:
        return json.load(src)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        state = load_state()
        body = json.dumps({"status": "ok", "served": state.get("served", 0)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
