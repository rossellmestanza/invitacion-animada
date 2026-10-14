import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for smooth media streaming
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.mjs'):
            return 'application/javascript'
        if path.endswith('.css'):
            return 'text/css'
        if path.endswith('.mp4'):
            return 'video/mp4'
        if path.endswith('.mp3'):
            return 'audio/mpeg'
        return super().guess_type(path)

# Ensure running in script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

while PORT < 8090:
    try:
        httpd = ThreadingServer(("", PORT), MyHandler)
        url = f"http://localhost:{PORT}/index.html"
        print("="*60, flush=True)
        print(f" Servidor iniciado con éxito!", flush=True)
        print(f" Abriendo en tu navegador: {url}", flush=True)
        print(f" También puedes probar la versión React en: http://localhost:{PORT}/app.html?template=royal-grace", flush=True)
        print(" Presiona Ctrl + C para detener el servidor.", flush=True)
        print("="*60, flush=True)
        webbrowser.open(url)
        httpd.serve_forever()
    except OSError:
        PORT += 1
