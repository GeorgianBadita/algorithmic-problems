dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def valid_coords(i, j, martrix):
    return i >= 0 and i < len(martrix) and j >= 0 and j < len(martrix[0])


def remove_island(i, j, matrix, value):
    queue = [(i, j)]
    matrix[i][j] = value

    while queue:
        i, j = queue.pop(0)

        for n in range(len(dx)):
            row, col = i + dx[n], j + dy[n]
            if valid_coords(row, col, matrix) and matrix[row][col] == 1:
                matrix[row][col] = value
                queue.append((row, col))


def removeIslands(matrix):

    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            remove_island(i, 0, matrix, 2)
        if matrix[i][len(matrix[0]) - 1] == 1:
            remove_island(i, len(matrix[0]) - 1, matrix, 2)

    for j in range(len(matrix[0])):
        if matrix[0][j] == 1:
            remove_island(0, j, matrix, 2)
        if matrix[len(matrix) - 1][j] == 1:
            remove_island(len(matrix) - 1, j, matrix, 2)

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 1:
                remove_island(i, j, matrix, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2:
                matrix[i][j] = 1

    return matrix


removeIslands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
])
