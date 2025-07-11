
from flask import Flask, jsonify, request
from flask_cors import CORS

import board
import player

app = Flask(__name__)
CORS(app)

BOARD = [None] * 9
CURRENT_PLAYER = player.generate_player("X")

@app.route("/api/move", methods=["POST"])
def make_move():
    global BOARD, CURRENT_PLAYER

    for p in ["X", "O"]:
        if board.check_for_win(BOARD, p):
            return jsonify({"error": "Game is over"}), 400
    if None not in BOARD:
        return jsonify({"error": "Game is over"}), 400

    data = request.get_json()
    loc = data.get("location")

    if not (0 <= loc < 9) or BOARD[loc] is not None:
        return jsonify({"error": "Invalid move"}), 400

    BOARD[loc] = CURRENT_PLAYER

    winner = board.check_for_win(BOARD, CURRENT_PLAYER)
    is_draw = None not in BOARD and not winner

    if not winner and not is_draw:
        CURRENT_PLAYER = player.change_player(CURRENT_PLAYER)

    return jsonify({
        "board": BOARD,
        "winner": winner,
        "is_draw": is_draw,
        "current_player": CURRENT_PLAYER
    })

@app.route("/api/reset", methods=["POST"])
def reset_game():
    global BOARD, CURRENT_PLAYER
    BOARD = [None] * 9
    CURRENT_PLAYER = player.generate_player("X")
    return jsonify({"board": BOARD, "current_player": CURRENT_PLAYER})

if __name__ == "__main__":
    app.run(debug=True)
