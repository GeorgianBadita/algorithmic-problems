def valid_coords(board, i, j):
    return i >= 0 and i < len(board) and j >= 0 and j < len(board[0])


def check_word(board, i, j, word):
    if not word:
        return True

    if board[i][j] != word[0]:
        return False

    dx = [1, 0, 0, -1, 1, -1, -1, 1]
    dy = [0, 1, -1, 0, 1, -1, 1, -1]

    current_value = board[i][j]
    apperas = False

    for direction in range(8):
        dir_x = dx[direction]
        dir_y = dy[direction]
        board[i][j] = "_"
        if valid_coords(board, i + dir_x, j + dir_y):
            apperas = apperas | check_word(
                board, i + dir_x, j + dir_y, word[1:])
    board[i][j] = current_value
    return apperas


def word_apperas_on_board(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if check_word(board, i, j, word):
                return True
    return False


def boggleBoard(board, words):
    return [word for word in words if word_apperas_on_board(board, word)]
