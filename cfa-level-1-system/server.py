import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.md'] = 'text/markdown'

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Server at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
