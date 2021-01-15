def valid_pos(i, j, arr):
    return i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0])


def get_diag(i, j, arr, flip, result):
    curr_res = []
    while valid_pos(i, j, arr):
        if not flip:
            curr_res.append(arr[i][j])
        else:
            curr_res.insert(0, arr[i][j])

        i -= 1
        j += 1
    result += curr_res


def zigzagTraverse(array):
    first_row = 0
    first_col = 0
    result = []
    last_flip_state = True
    while first_row < len(array):
        get_diag(first_row, first_col, array, last_flip_state, result)
        first_row += 1
        last_flip_state = not last_flip_state

    first_row = len(array) - 1
    first_col = 1

    while first_col < len(array[0]):
        get_diag(first_row, first_col, array, last_flip_state, result)
        first_col += 1
        last_flip_state = not last_flip_state

    return result
