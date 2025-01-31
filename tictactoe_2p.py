# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")

# Function to check for a winner
def check_winner(player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                      (0,3,6), (1,4,7), (2,5,8),  # Columns
                      (0,4,8), (2,4,6)]           # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full (Draw)
def is_full():
    return " " not in board

# Function to take player input
def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    for turn in range(9):
        current_player = "X" if turn % 2 == 0 else "O"
        player_move(current_player)
        print_board()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        if is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
