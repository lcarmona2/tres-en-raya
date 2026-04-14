from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    return None

def reset():
    return [""] * 9

@app.route ('/', Methods=['GET'])
def index():
    build_dir = os.path.join(os.path.dirname(__file__), "frontend", "build")
    index_path = os.path.join(build_dir, "index.html")

    if os.path.exists(index_path):
        return send_from_directory(build_dir, "index.html")
    else:
        return "⚙️ PQC API is running (sin frontend build)", 200

@app.route("/move", methods=["POST"])
def move():
    board = request.json["board"]
    winner = check_winner(board)

    return jsonify({
        "winner": winner
    })

@app.route("/reset", methods=["POST"])
def reset_game():
    return jsonify({
        "board": reset()
    })
    

if __name__ == "__main__":
    app.run(debug=True)