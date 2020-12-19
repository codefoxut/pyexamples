import copy


def get_prefilled_positions(board) -> set:
    prefilled_pos = set()
    for row, row_items in enumerate(board):
        for col, item in enumerate(row_items):
            if item != " ":
                prefilled_pos.add((row, col))
    return prefilled_pos


def get_empty_board() -> list:
    return [[" "] * 9 for _ in range(9)]


def display_board(board):
    for i in board:
        print("|".join([f"{x}" for x in i]))
        print("_".join([" " for _ in i]))


def is_constraint_satisfying(n: int, num: int, row: int, col: int, board: list):
    board[row][col] = " "
    # check for all cols
    for i in range(n):
        if board[row][i] == num:
            return False
    # check for all rows
    for i in range(n):
        if board[i][col] == num:
            return False
    # check the 3x3 block.
    row_idx = row // 3 * 3
    col_idx = col // 3 * 3
    for i in range(row_idx, row_idx + 3):
        for j in range(col_idx, col_idx + 3):
            if board[i][j] == num:
                return False
    return True


def find_next_slot_to_fill(n, row, col, prefilled_slots):
    def overlap_row(n, i, j):
        if j == n:
            i, j = i + 1, 0
        return i, j
    nxt_row, nxt_col = row, col + 1
    nxt_row, nxt_col = overlap_row(n, nxt_row, nxt_col)
    while (nxt_row, nxt_col) in prefilled_slots:
        nxt_row, nxt_col = nxt_row, nxt_col + 1
        nxt_row, nxt_col = overlap_row(n, nxt_row, nxt_col)
    # print(f"find next row {row} col {col} -> row {nxt_row} col {nxt_col}")
    return nxt_row, nxt_col


def sudoku_solver(n: int, row: int, col: int, board: list, prefilled_slots: set):
    # check and fill the number
    # call for next element.
    # print(f"row {row} col {col}")
    resp = None
    for i in range(1, n + 1):
        if (row, col) in prefilled_slots:
            next_element = True
        elif is_constraint_satisfying(n, i, row, col, board):
            # print(f"constraint satisfied row {row} col {col} num {i}")
            board[row][col] = i
            next_element = True
        else:
            next_element = False

        if next_element:
            # display_board(board)
            if row + 1 == n and col + 1 == n:
                return True
            else:
                nxt_row, nxt_col = find_next_slot_to_fill(n, row, col, prefilled_slots)
                resp = sudoku_solver(n, nxt_row, nxt_col, board, prefilled_slots)
                if resp is not True:
                    board[row][col] = " "
                else:
                    return resp

    return resp


if __name__ == "__main__":
    sb: list = get_empty_board()
    # sudoku 1
    sb[0][2] = 4
    sb[1][4], sb[1][6], sb[1][7], sb[1][8] = 7, 3, 4, 2
    sb[2][0], sb[2][4], sb[2][5], sb[2][7] = 1, 8, 4, 5
    sb[3][3], sb[3][4], sb[3][7] = 9, 5, 8
    sb[4][2], sb[4][6] = 5, 1
    sb[5][1], sb[5][4], sb[5][5] = 9, 3, 6
    sb[6][1], sb[6][3], sb[6][4], sb[6][8] = 7, 8, 1, 6
    sb[7][0], sb[7][1], sb[7][2], sb[7][4] = 6, 8, 9, 2
    sb[8][6] = 4
    display_board(sb)
    prefilled_slots = get_prefilled_positions(sb)
    sb1 = copy.deepcopy(sb)
    resp1 = sudoku_solver(9, 0, 0, sb1, prefilled_slots)
    print("final response")
    display_board(sb1)
    # sudoku 2
    su2: list = get_empty_board()
    su2[0][2], su2[0][3], su2[0][4], su2[0][8] = 8, 5, 9, 3
    su2[1][1], su2[1][3], su2[1][6], su2[1][8] = 1, 4, 9, 8
    su2[2][7] = 6
    su2[3][0], su2[3][7] = 5, 1
    su2[4][0], su2[4][4], su2[4][8] = 7, 1, 6
    su2[5][1], su2[5][8] = 2, 9
    su2[6][1] = 8
    su2[7][0], su2[7][2], su2[7][5], su2[7][7] = 6, 7, 9, 2
    su2[8][0], su2[8][4], su2[8][5], su2[8][6] = 3, 7, 5, 6

    prefilled_slots2 = get_prefilled_positions(su2)
    sb1 = copy.deepcopy(su2)
    resp2 = sudoku_solver(9, 0, 0, sb1, prefilled_slots2)
    print("final response")
    display_board(sb1)
