from http.server import SimpleHTTPRequestHandler, HTTPServer
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        return super().end_headers()

if __name__ == '__main__':
    port = 8000  # Choose a port number
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)

    print(f'Server running on http://localhost:{port}/ (Press Ctrl+C to stop)')
    httpd.serve_forever()
