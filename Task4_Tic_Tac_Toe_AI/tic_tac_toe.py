import math
import random


# -----------------------------
# Display the Board
# -----------------------------

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


# -----------------------------
# Check Winner
# -----------------------------

def check_winner(board):

    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:

        if board[a] == board[b] == board[c]:
            return board[a]

    if all(position in ["X", "O"] for position in board):
        return "Draw"

    return None


# -----------------------------
# Available Moves
# -----------------------------

def get_available_moves(board):
    return [
        i for i, position in enumerate(board)
        if position not in ["X", "O"]
    ]


# -----------------------------
# Minimax Algorithm
# -----------------------------

def minimax(board, depth, maximizing, alpha=-math.inf, beta=math.inf):

    result = check_winner(board)

    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    if maximizing:

        best_score = -math.inf

        for move in get_available_moves(board):

            board[move] = "O"

            score = minimax(
                board,
                depth + 1,
                False,
                alpha,
                beta
            )

            board[move] = str(move + 1)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score

    else:

        best_score = math.inf

        for move in get_available_moves(board):

            board[move] = "X"

            score = minimax(
                board,
                depth + 1,
                True,
                alpha,
                beta
            )

            board[move] = str(move + 1)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best_score

# -----------------------------
# AI Move
# -----------------------------

def get_best_move(board):

    best_score = -math.inf
    best_move = None

    for move in get_available_moves(board):

        board[move] = "O"

        score = minimax(
            board,
            0,
            False,
            -math.inf,
            math.inf
        )

        board[move] = str(move + 1)

        if score > best_score:

            best_score = score
            best_move = move

    return best_move


# -----------------------------
# Difficulty Level
# -----------------------------

def get_ai_move(board, difficulty):

    if difficulty == "easy":

        return random.choice(get_available_moves(board))

    elif difficulty == "medium":

        if random.random() < 0.5:
            return random.choice(get_available_moves(board))

        return get_best_move(board)

    else:

        return get_best_move(board)


# -----------------------------
# Main Game
# -----------------------------

def play_game():

    board = [str(i) for i in range(1, 10)]

    print("===================================")
    print("       TIC-TAC-TOE AI")
    print("===================================")

    print("\nYou are X.")
    print("The AI is O.")

    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    difficulty_choice = input("\nEnter choice: ")

    if difficulty_choice == "1":
        difficulty = "easy"

    elif difficulty_choice == "2":
        difficulty = "medium"

    else:
        difficulty = "hard"

    print(f"\nDifficulty selected: {difficulty.upper()}")

    print("\nBoard positions:")

    print_board(board)

    while True:

        # -----------------------------
        # Human Turn
        # -----------------------------

        try:

            move = int(input("Choose a position (1-9): ")) - 1

            if move not in get_available_moves(board):

                print("Invalid move. Try again.")
                continue

            board[move] = "X"

        except ValueError:

            print("Please enter a number between 1 and 9.")
            continue

        print_board(board)

        result = check_winner(board)

        if result:

            break

        # -----------------------------
        # AI Turn
        # -----------------------------

        print("AI is thinking...")

        ai_move = get_ai_move(board, difficulty)

        board[ai_move] = "O"

        print(f"AI selected position {ai_move + 1}")

        print_board(board)

        result = check_winner(board)

        if result:

            break

    # -----------------------------
    # Game Result
    # -----------------------------

    if result == "X":

        print("🎉 You won!")

    elif result == "O":

        print("AI wins!")

    else:

        print("It's a draw!")


# -----------------------------
# Start Game
# -----------------------------

if __name__ == "__main__":
    play_game()