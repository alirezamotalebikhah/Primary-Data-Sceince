import random

# Initialize board (list of lists)
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    """Prints the board with indexes"""
    print("   0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)

def is_winner(player):
    """Check if the given player has won"""
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full():
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)

def get_empty_positions():
    """Return a list of empty (row,col) positions"""
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def play_game():
    """Main game loop with CPU"""
    player = "X"
    cpu = "O"

    while True:
        print_board()

        # Player's turn
        try:
            row = int(input("Player X, enter row (0-2): "))
            col = int(input("Player X, enter col (0-2): "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if (row not in [0,1,2]) or (col not in [0,1,2]):
            print("❌ Invalid position! Row and Col must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("❌ Position already taken! Try again.")
            continue

        board[row][col] = player

        # Check if player wins
        if is_winner(player):
            print_board()
            print("🎉 You win!")
            break

        if is_full():
            print_board()
            print("🤝 It's a draw!")
            break

        # CPU's turn
        print("\n🤖 CPU is thinking...")
        empty_positions = get_empty_positions()
        row, col = random.choice(empty_positions)
        board[row][col] = cpu

        # Check if CPU wins
        if is_winner(cpu):
            print_board()
            print("💻 CPU wins!")
            break

        if is_full():
            print_board()
            print("🤝 It's a draw!")
            break


# Run the game
play_game()
