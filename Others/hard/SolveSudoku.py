def solveSudoku(board):
    solve_aux(0, 0, board)
    return board


def solve_aux(row, col, board):
    curr_row = row
    curr_col = col

    if curr_col == len(board[0]):
        curr_row += 1
        curr_col = 0
        if curr_row == len(board):
            return True

    if board[curr_row][curr_col] == 0:
        return map_digit(curr_row, curr_col, board)

    return solve_aux(curr_row, curr_col + 1, board)


def map_digit(curr_row, curr_col, board):
    for i in range(1, 10):
        if consistent_board(curr_row, curr_col, board, i):
            board[curr_row][curr_col] = i
            if solve_aux(curr_row, curr_col + 1, board):
                return True
    board[curr_row][curr_col] = 0
    return False


def consistent_board(row, col, board, value):
    is_row_valid = value not in board[row]
    is_col_valid = value not in map(lambda r: r[col], board)

    if not is_col_valid or not is_row_valid:
        return False

    r_start = (row // 3) * 3
    c_start = (col // 3) * 3

    for r_idx in range(3):
        for c_idx in range(3):
            r = r_start + r_idx
            c = c_start + c_idx

            val = board[r][c]

            if val == value:
                return False
    return True


board = [
    [0, 2, 0, 0, 9, 0, 1, 0, 0],
    [0, 0, 7, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 6, 0],
    [0, 0, 1, 9, 0, 4, 0, 0, 0],
    [0, 0, 0, 6, 0, 5, 0, 0, 7],
    [8, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 8, 5],
    [4, 9, 0, 0, 3, 0, 0, 0, 0]
]

print(solveSudoku(board))
