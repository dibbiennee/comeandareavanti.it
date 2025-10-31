
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/attached_assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('attached_assets', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
