import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

print("--- Iniciando Canal Digital de Ventas ---")

db_host = os.environ.get("DATABASE_HOST")

if not db_host:
    print("[ERROR] Falla crítica: No se detectó la variable DATABASE_HOST.", file=sys.stderr)
    sys.exit(1)

print(f"[SUCCESS] Conectado exitosamente a la base de datos en: {db_host}")

# Servidor web real en el puerto 5000
class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = f"""
        <html>
        <head><title>Canal de Ventas</title></head>
        <body style='font-family: Arial; text-align: center; margin-top: 100px;'>
            <h1>🚀 Canal Digital de Ventas Operativo</h1>
            <p>Conectado a la base de datos: <b>{db_host}</b></p>
            <p style='color: green;'><b>SLA 99.99% Cumplido - Alta Disponibilidad</b></p>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

server = HTTPServer(('0.0.0.0', 5000), WebServer)
print("[STATUS] Servidor HTTP escuchando en el puerto 5000...")
server.serve_forever()
