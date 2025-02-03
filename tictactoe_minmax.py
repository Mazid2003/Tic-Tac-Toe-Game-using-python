import math
import time

# Function to initialize the board
def initialize_board():
    return [" " for _ in range(9)]

# Function to print the styled board
def print_board(board):
    print("\n")
    print("  ┌───┬───┬───┐")
    for i in range(0, 9, 3):
        print(f"  │ {board[i]} │ {board[i+1]} │ {board[i+2]} │")
        if i < 6:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘\n")

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full
def is_full(board):
    return " " not in board

# Function to evaluate board score (Minimax)
def evaluate(board):
    if check_winner(board, "O"):  # AI wins
        return 1
    elif check_winner(board, "X"):  # Player wins
        return -1
    return 0  # Draw

# Minimax algorithm for optimal AI moves
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1:
        return score
    if is_full(board):
        return 0  # Draw

    if is_maximizing:  # AI's turn (maximizer)
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # AI makes a move
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = " "  # Undo move
        return best_score
    else:  # Player's turn (minimizer)
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Player makes a move
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = " "  # Undo move
        return best_score

# AI chooses the best move using Minimax
def computer_move(board):
    print("\n🤖 Computer is thinking...")
    time.sleep(1)  # Simulating AI's thinking time
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Try move
            move_score = minimax(board, 0, False)
            board[i] = " "  # Undo move

            if move_score > best_score:
                best_score = move_score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"

# Function for the player's move
def player_move(board):
    while True:
        try:
            move = int(input("\n🎯 Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("❌ Invalid move! That spot is taken or out of range. Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number between 1-9.")

# Main game loop
def play_game():
    while True:
        board = initialize_board()
        print("\n🎮 Welcome to Tic-Tac-Toe! 🎮")
        print("🔹 You are 'X' | 🤖 AI is 'O'")
        print_board(board)

        while True:
            # Player's turn
            player_move(board)
            print_board(board)
            if check_winner(board, "X"):
                print("\n🎉 Congratulations! You win! 🎉")
                break
            if is_full(board):
                print("\n🤝 It's a draw! Well played.")
                break

            # AI's turn
            computer_move(board)
            print_board(board)
            if check_winner(board, "O"):
                print("\n💻 Computer wins! Better luck next time! 😢")
                break
            if is_full(board):
                print("\n🤝 It's a draw! Well played.")
                break

        # Ask if the player wants to play again
        while True:
            restart = input("\n🔄 Do you want to play again? (y/n): ").strip().lower()
            if restart == 'y':
                break
            elif restart == 'n':
                print("\n👋 Thanks for playing! Goodbye!")
                return
            else:
                print("⚠️ Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    play_game()
