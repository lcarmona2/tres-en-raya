from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# 🆕 Contador global de victorias
scores = {
    "X": 0,
    "O": 0
}

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]

    return None

def reset():
    return [""] * 9

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route("/move", methods=["POST"])
def move():
    board = request.json["board"]
    winner = check_winner(board)

    # 🆕 Si hay ganador, sumamos punto
    if winner in scores:
        scores[winner] += 1

    return jsonify({
        "winner": winner,
        "scores": scores
    })

@app.route("/reset", methods=["POST"])
def reset_game():
    return jsonify({
        "board": reset()
    })

# 🆕 Obtener marcador
@app.route("/scores", methods=["GET"])
def get_scores():
    return jsonify(scores)

# 🆕 Resetear marcador
@app.route("/reset_scores", methods=["POST"])
def reset_scores():
    global scores
    scores = {"X": 0, "O": 0}
    return jsonify(scores)

print("Servidor de Tres en Raya iniciado en http://localhost:5000")

if __name__ == "__main__":
    app.run(debug=True)