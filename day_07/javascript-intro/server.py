import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Deshabilitar caché para desarrollo
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    """Servir la página principal (index.html)"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    """Servir cualquier archivo estático"""
    return send_from_directory('.', path)

@app.after_request
def add_header(response):
    """Añadir headers para deshabilitar caché"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Servidor de desarrollo iniciado")
    print("="*50)
    print("📂 Carpeta: javascript-intro")
    print("🌐 URL: http://localhost:3000")
    print("💡 Presiona Ctrl+C para detener el servidor")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=3000, debug=True)
