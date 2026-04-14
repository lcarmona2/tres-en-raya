from flask import Flask, request, jsonify
import random

app = Flask(__name__, static_folder='../frontend', static_url_path='')

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

# 👉 FUNCIÓN NUEVA (IA muy básica)
def bot_move(board):
    for i in range(9):
        if board[i] == "":
            board[i] = "O"  # la IA juega con O
            return board
    return board

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route("/move", methods=["POST"])
def move():
    board = request.json["board"]

    # comprobar si ya hay ganador antes del bot
    ganador = check_winner(board)

    if not ganador:
        board = bot_move(board)  # 👉 movimiento automático

    ganador = check_winner(board)

    return jsonify({
        "board": board,
        "winner": ganador
    })

@app.route("/reset", methods=["POST"])
def reset_game():
    return jsonify({
        "board": reset()
    })

print("Hello world")

if __name__ == "__main__":
    app.run(debug=True)