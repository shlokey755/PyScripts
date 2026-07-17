def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()


