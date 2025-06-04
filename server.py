from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Все запросы перенаправляем на contacts.html
        file_path = os.path.join('templates', 'contacts.html')

        if not os.path.exists(file_path):
            self.send_error(404, "File not found")
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        with open(file_path, 'rb') as file:
            self.wfile.write(file.read())


def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8000')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
