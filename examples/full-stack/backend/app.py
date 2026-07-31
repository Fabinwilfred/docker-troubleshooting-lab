from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def root():
    return "OK from backend"

@app.route('/api/')
def api_root():
    return jsonify({"status": "ok", "service": "api"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
