from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Write the response body
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080

    # Create and start the server
    server = HTTPServer((host, port), HelloHandler)
    print(f"Server running at http://{host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        server.server_close()
