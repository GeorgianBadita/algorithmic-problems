def searchInSortedMatrix(matrix, target):
    current_row = len(matrix) - 1
    current_col = 0

    while current_col >= 0 and current_col < len(matrix[0]) and current_row >= 0 and current_row < len(matrix):
        if matrix[current_row][current_col] == target:
            return [current_row, current_col]

        if matrix[current_row][current_col] > target:
            current_row -= 1
        else:
            current_col += 1

    return [-1, -1]
