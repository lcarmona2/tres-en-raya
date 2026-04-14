from flask import Flask, request, jsonify

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

@app.route("/move", methods=["POST"])
def move():
    board = request.json["board"]
    winner = check_winner(board)

    return jsonify({
        "winner": winner
    })

if __name__ == "__main__":
    app.run(debug=True)