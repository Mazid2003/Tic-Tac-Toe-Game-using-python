# 1️⃣ Simple Player vs. Computer Tic-Tac-Toe (Random AI)

**📌 Features:**

Board Representation: A list of 9 elements (3x3 grid).

User Move: The player enters a number (1-9) to place their mark (X).

Computer Move: The computer picks a random empty cell and places O.

Win Check: The game checks for row, column, or diagonal matches.

Draw Condition: If the board is full and no winner, it's a draw.

**🛠️ Implementation Details:**

print_board(): Displays the Tic-Tac-Toe board.

check_winner(player): Checks if a player has won.

is_full(): Checks if the board is full.

player_move(): Takes user input and validates the move.

computer_move(): Picks a random available cell for the AI.

play_game(): Main game loop handling user and AI turns.

✅ Possible Enhancement: Improve AI using Minimax (covered in the next version).

# 2️⃣ Tic-Tac-Toe with AI (Minimax Algorithm)

**📌 Features:**

AI Uses Minimax: The computer plays optimally using the Minimax algorithm, which evaluates the best possible move to never lose.

No Random Moves: Unlike the previous version, the AI now makes intelligent decisions.

Win, Loss, and Draw Handling: Just like before, the game announces results based on board conditions.

**🛠️ Implementation Details:**

evaluate(): Assigns a score (+1 for AI win, -1 for player win, 0 for draw).

minimax(depth, is_maximizing):

Recursive function that simulates all possible future moves and picks the best one.

AI (Maximizing) tries to maximize score.

Player (Minimizing) tries to minimize score.

computer_move(): AI selects the best possible move using Minimax.

**🤖 Why Minimax?**

Instead of random moves, the AI predicts the best outcome for every possible move.

The AI never loses unless the opponent also plays perfectly.

✅ Possible Enhancement: Add Alpha-Beta Pruning to optimize Minimax for faster decision-making.

# 3️⃣ Two-Player Tic-Tac-Toe (No AI, Just Multiplayer)

**📌 Features:**

Two-player game (X vs O) with alternating turns.

Players manually enter moves instead of playing against AI.

Basic game loop that continuously checks for wins or draws.

**🛠️ Implementation Details:**

player_move(player): Takes input from Player X or O.

check_winner(player): Checks if any player has won.

play_game(): Alternates turns between Player X and Player O.

**💡 Final Thoughts**

Each version serves a different purpose:

Version 1: Simple Tic-Tac-Toe with random AI (Beginner Level).

Version 2: Advanced AI using Minimax (Intermediate Level).

Version 3: Multiplayer Tic-Tac-Toe (for two human players).

**💬 Want to Collaborate?**

Feel free to fork the repo, submit PRs, and give your feedback! 🔥💡

**📜 License**

This project is open-source under the MIT License. Feel free to use and
modify it! 🚀
