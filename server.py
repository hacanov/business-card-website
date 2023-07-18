import http.server
import socketserver
from typing import Self


PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('word.html', 'rb') as file:
                    self.wfile.write(file.read())
        elif self.path == '/css1.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('css1.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/java.js':
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            with open('java.js', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404)

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Server started on port', PORT)
    httpd.serve_forever()