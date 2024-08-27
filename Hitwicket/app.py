# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# # Game state initialization
# game_state = {
#     "current_player": "A",
#     "board": [
#         ["A-P1", "A-H1", "A-H2", "A-H3", "A-P2"],
#         ["", "", "", "", ""],
#         ["", "", "", "", ""],
#         ["", "", "", "", ""],
#         ["B-P1", "B-H1", "B-H2", "B-H3", "B-P2"]
#     ],
#     "players": {
#         "A": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(0, 0), (0, 4), (0, 1), (0, 2), (0, 3)]},
#         "B": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(4, 0), (4, 4), (4, 1), (4, 2), (4, 3)]}
#     }
# }

# def is_valid_position(x, y):
#     return 0 <= x < 5 and 0 <= y < 5

# def get_piece(player, char_type):
#     return f"{player}-{char_type}"

# def is_opponent_piece(piece, current_player):
#     return piece.startswith("A-") if current_player == "B" else piece.startswith("B-")

# def move_piece(current_player, character, direction):
#     positions = game_state["players"][current_player]["positions"]
#     board = game_state["board"]
#     idx = game_state["players"][current_player]["characters"].index(character)
#     x, y = positions[idx]
#     new_x, new_y = x, y

#     if character == "P1" or character == "P2":
#         if direction == "L": new_y -= 1
#         elif direction == "R": new_y += 1
#         elif direction == "F": new_x -= 1 if current_player == "A" else new_x + 1
#         elif direction == "B": new_x += 1 if current_player == "A" else new_x - 1
#     elif character == "H1":
#         if direction == "L": new_y -= 2
#         elif direction == "R": new_y += 2
#         elif direction == "F": new_x -= 2 if current_player == "A" else new_x + 2
#         elif direction == "B": new_x += 2 if current_player == "A" else new_x - 2
#     elif character == "H2":
#         if direction == "FL": new_x, new_y = x - 2, y - 2
#         elif direction == "FR": new_x, new_y = x - 2, y + 2
#         elif direction == "BL": new_x, new_y = x + 2, y - 2
#         elif direction == "BR": new_x, new_y = x + 2, y + 2

#     if not is_valid_position(new_x, new_y):
#         return "Invalid move: Out of bounds."

#     if board[new_x][new_y] and not is_opponent_piece(board[new_x][new_y], current_player):
#         return "Invalid move: Cannot capture own piece."

#     if character in ["H1", "H2"] and board[new_x][new_y] and is_opponent_piece(board[new_x][new_y], current_player):
#         board[new_x][new_y] = ""

#     board[x][y] = ""
#     board[new_x][new_y] = get_piece(current_player, character)
#     positions[idx] = (new_x, new_y)

#     game_state["current_player"] = "B" if current_player == "A" else "A"

#     winner = check_winner()
#     if winner:
#         return f"Game Over. Player {winner} wins!"

#     return "Move successful."

# def check_winner():
#     for player in ["A", "B"]:
#         if all(piece.startswith(f"{player}-") for piece in game_state["board"][0] + game_state["board"][4]):
#             return "A" if player == "B" else "B"
#     return None

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/move", methods=["POST"])
# def move():
#     data = request.json
#     current_player = game_state["current_player"]
#     character = data.get("character")
#     direction = data.get("direction")

#     if character not in game_state["players"][current_player]["characters"]:
#         return jsonify({"message": "Invalid character for current player."})

#     message = move_piece(current_player, character, direction)

#     return jsonify({"message": message, "game_state": game_state})

# if __name__ == "__main__":
#     app.run(debug=True)

 
##   CODE - 1  - WORKING CODE

# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# # Game state initialization
# game_state = {
#     "current_player": "A",
#     "board": [
#         ["A-P1", "A-H1", "A-H2", "A-H3", "A-P2"],
#         ["", "", "", "", ""],
#         ["", "", "", "", ""],
#         ["", "", "", "", ""],
#         ["B-P1", "B-H1", "B-H2", "B-H3", "B-P2"]
#     ],
#     "players": {
#         "A": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(0, 0), (0, 4), (0, 1), (0, 2), (0, 3)]},
#         "B": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(4, 0), (4, 4), (4, 1), (4, 2), (4, 3)]}
#     },
#     "move_history": []
# }

# def is_valid_position(x, y):
#     return 0 <= x < 5 and 0 <= y < 5

# def get_piece(player, char_type):
#     return f"{player}-{char_type}"

# def is_opponent_piece(piece, current_player):
#     return piece.startswith("A-") if current_player == "B" else piece.startswith("B-")

# def move_piece(current_player, character, direction):
#     positions = game_state["players"][current_player]["positions"]
#     board = game_state["board"]
#     idx = game_state["players"][current_player]["characters"].index(character)
#     x, y = positions[idx]
#     new_x, new_y = x, y

#     # Determine new position based on character and direction
#     if character in ["P1", "P2"]:  # Pawn movements
#         if direction == "L": new_y -= 1
#         elif direction == "R": new_y += 1
#         elif direction == "F": new_x -= 1 if current_player == "A" else new_x + 1
#         elif direction == "B": new_x += 1 if current_player == "A" else new_x - 1
#     elif character == "H1":  # Horizontal Hero movements
#         if direction == "L": new_y -= 2
#         elif direction == "R": new_y += 2
#         elif direction == "F": new_x -= 2 if current_player == "A" else new_x + 2
#         elif direction == "B": new_x += 2 if current_player == "A" else new_x - 2
#     elif character == "H2":  # Diagonal Hero movements
#         if direction == "FL": new_x, new_y = x - 2, y - 2
#         elif direction == "FR": new_x, new_y = x - 2, y + 2
#         elif direction == "BL": new_x, new_y = x + 2, y - 2
#         elif direction == "BR": new_x, new_y = x + 2, y + 2

#     # Check if the new position is within bounds
#     if not is_valid_position(new_x, new_y):
#         return "Invalid move: Out of bounds."

#     # Check if the move lands on a player's own piece
#     if board[new_x][new_y] and not is_opponent_piece(board[new_x][new_y], current_player):
#         return "Invalid move: Cannot capture own piece."

#     # If the move captures an opponent's piece
#     if character in ["H1", "H2"] and board[new_x][new_y] and is_opponent_piece(board[new_x][new_y], current_player):
#         board[new_x][new_y] = ""  # Capture the opponent's piece

#     # Update the board and character positions
#     board[x][y] = ""
#     board[new_x][new_y] = get_piece(current_player, character)
#     positions[idx] = (new_x, new_y)

#     # Update move history
#     game_state["move_history"].append({
#         "player": current_player,
#         "character": character,
#         "from": (x, y),
#         "to": (new_x, new_y),
#         "direction": direction
#     })

#     # Switch to the next player
#     game_state["current_player"] = "B" if current_player == "A" else "A"

#     # Check if there is a winner
#     winner = check_winner()
#     if winner:
#         return f"Game Over. Player {winner} wins!"

#     return "Move successful."

# def check_winner():
#     # Check if one player has reached the opposite end of the board
#     for player in ["A", "B"]:
#         if all(piece.startswith(f"{player}-") for piece in game_state["board"][0] + game_state["board"][4]):
#             return "A" if player == "B" else "B"
#     return None

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/move", methods=["POST"])
# def move():
#     data = request.json
#     current_player = game_state["current_player"]
#     character = data.get("character")
#     direction = data.get("direction")

#     if character not in game_state["players"][current_player]["characters"]:
#         return jsonify({"status": "error", "message": "Invalid character for current player."})

#     message = move_piece(current_player, character, direction)
#     return jsonify({"status": "success", "message": message, "game_state": game_state})

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game state initialization
game_state = {
    "current_player": "A",
    "board": [
        ["A-P1", "A-H1", "A-H2", "A-H3", "A-P2"],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["B-P1", "B-H1", "B-H2", "B-H3", "B-P2"]
    ],
    "players": {
        "A": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(0, 0), (0, 4), (0, 1), (0, 2), (0, 3)]},
        "B": {"score": 0, "characters": ["P1", "P2", "H1", "H2", "H3"], "positions": [(4, 0), (4, 4), (4, 1), (4, 2), (4, 3)]}
    },
    "move_history": []
}

def is_valid_position(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def get_piece(player, char_type):
    return f"{player}-{char_type}"

def is_opponent_piece(piece, current_player):
    return piece.startswith("A-") if current_player == "B" else piece.startswith("B-")

def move_piece(current_player, character, direction):
    positions = game_state["players"][current_player]["positions"]
    board = game_state["board"]
    idx = game_state["players"][current_player]["characters"].index(character)
    x, y = positions[idx]
    new_x, new_y = x, y

    if character == "P1" or character == "P2":
        if direction == "L": new_y -= 1
        elif direction == "R": new_y += 1
        elif direction == "F": new_x -= 1 if current_player == "A" else new_x + 1
        elif direction == "B": new_x += 1 if current_player == "A" else new_x - 1
    elif character == "H1":
        if direction == "L": new_y -= 2
        elif direction == "R": new_y += 2
        elif direction == "F": new_x -= 2 if current_player == "A" else new_x + 2
        elif direction == "B": new_x += 2 if current_player == "A" else new_x - 2
    elif character == "H2":
        if direction == "FL": new_x, new_y = x - 2, y - 2
        elif direction == "FR": new_x, new_y = x - 2, y + 2
        elif direction == "BL": new_x, new_y = x + 2, y - 2
        elif direction == "BR": new_x, new_y = x + 2, y + 2

    if not is_valid_position(new_x, new_y):
        return "Invalid move: Out of bounds."

    if board[new_x][new_y] and not is_opponent_piece(board[new_x][new_y], current_player):
        return "Invalid move: Cannot capture own piece."

    if character in ["H1", "H2"] and board[new_x][new_y] and is_opponent_piece(board[new_x][new_y], current_player):
        board[new_x][new_y] = ""

    board[x][y] = ""
    board[new_x][new_y] = get_piece(current_player, character)
    positions[idx] = (new_x, new_y)

    game_state["current_player"] = "B" if current_player == "A" else "A"

    # Record move history
    move_entry = {
        "player": current_player,
        "character": character,
        "direction": direction,
        "from": f"({x}, {y})",
        "to": f"({new_x}, {new_y})"
    }
    game_state["move_history"].append(move_entry)

    winner = check_winner()
    if winner:
        return f"Game Over. Player {winner} wins!"

    return "Move successful."

def check_winner():
    for player in ["A", "B"]:
        if all(piece.startswith(f"{player}-") for piece in game_state["board"][0] + game_state["board"][4]):
            return "A" if player == "B" else "B"
    return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    current_player = game_state["current_player"]
    character = data.get("character")
    direction = data.get("direction")

    if character not in game_state["players"][current_player]["characters"]:
        return jsonify({"status": "error", "message": "Invalid character for current player."})

    message = move_piece(current_player, character, direction)
    return jsonify({"status": "success", "message": message, "game_state": game_state, "move_history": game_state["move_history"]})

if __name__ == "__main__":
    app.run(debug=True)
