#!/usr/bin/env python3
"""
Simple HTTP server with CORS headers for love.js testing.
Adds Cross-Origin-Opener-Policy and Cross-Origin-Embedder-Policy headers
required for SharedArrayBuffer support.
"""
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8888

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()
    
    def guess_type(self, path):
        if path.endswith('.wasm'):
            return 'application/wasm'
        return super().guess_type(path)

with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
