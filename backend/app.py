from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)  # Enable CORS for all routes

# Define a route for the root URL
@app.route('/')
def index():
    return jsonify({"message": "Hello from Flask!"})

# Serve the React build files
@app.route('/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
