import flask
import os
from flask import send_from_directory

from tres_en_raya import move, reset

app = flask.Flask(__name__)

@app.route ('/', Methods=['GET'])
def index():
    build_dir = os.path.join(os.path.dirname(__file__), "frontend", "build")
    index_path = os.path.join(build_dir, "index.html")

    if os.path.exists(index_path):
        return send_from_directory(build_dir, "index.html")
    else:
        return "⚙️ PQC API is running (sin frontend build)", 200
    
@app.route('/move', methods=['POST'])
def make_move():
    data = flask.request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    move(row, col)

    return "Move made successfully", 200

@app.route('/reset', methods=['GET'])
def reset_game():
    # Implementation for handling reset requests
    reset()
    
    return "Game reset successfully", 200

if __name__ == "__main__":
    app.run(debug=True)
    
