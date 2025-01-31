import random

# Initialize board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

# Function to check for a win
def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), # Rows
                      (0,3,6), (1,4,7), (2,5,8), # Columns
                      (0,4,8), (2,4,6)]         # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full
def is_full():
    return " " not in board

# Function to get player's move
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

# Function for computer's move
def computer_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_cells)
    board[move] = "O"

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player move
        player_move()
        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        # Computer move
        print("Computer is making a move...")
        computer_move()
        print_board()
        if check_winner("O"):
            print("💻 Computer wins!")
            break
        if is_full():
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
