import copy


def n_queen_solver(n: int):
    sample_board = [[0]* n for _ in range(n)]
    sol_boards = []
    queen_helper(n, 0, sample_board, sol_boards)
    print(f"no of solutions found: {len(sol_boards)}")


def print_board(board: list, i=None, j=None):
    if i is None and j is None:
        print("printing Final board.")
    else:
        print(f"printing at row {i}, col {j}")
    for i in board:
        print(" ".join([f"{x}" for x in i]))


def queen_helper(n: int, row: int, board: list, sol_boards: list):
    if row != n:
        for j in range(n):
            if is_possible(n, row, j, board):
                board[row][j] = 1
                print_board(board, row, j)
                print(f"Trying row {row+1} now")
                queen_helper(n, row+1, board, sol_boards)

            board[row][j] = 0
    else:
        sol_boards.append(copy.deepcopy(board))
        print_board(board)


def is_possible(n: int, row: int, col: int, board: list):
    # same column (upper rows only)
    for i in range(row-1, -1, -1):
        if board[i][col] == 1:
            return False
    # upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True
