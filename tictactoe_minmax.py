import math

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

# Function to check for a winner
def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full
def is_full():
    return " " not in board

# Function to evaluate board score (Minimax)
def evaluate():
    if check_winner("O"):  # AI wins
        return 1
    elif check_winner("X"):  # Player wins
        return -1
    return 0  # Draw

# Minimax algorithm for optimal AI moves
def minimax(depth, is_maximizing):
    score = evaluate()

    # If the game is over, return the score
    if score == 1 or score == -1:
        return score
    if is_full():
        return 0  # Draw

    if is_maximizing:  # AI's turn (maximizer)
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # AI makes a move
                best_score = max(best_score, minimax(depth + 1, False))
                board[i] = " "  # Undo move
        return best_score
    else:  # Player's turn (minimizer)
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Player makes a move
                best_score = min(best_score, minimax(depth + 1, True))
                board[i] = " "  # Undo move
        return best_score

# AI chooses the best move using Minimax
def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Try move
            move_score = minimax(0, False)
            board[i] = " "  # Undo move

            if move_score > best_score:
                best_score = move_score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"

# Function for the player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        # AI's turn
        print("Computer is making a move...")
        computer_move()
        print_board()
        if check_winner("O"):
            print("💻 Computer wins!")
            break
        if is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
