dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def valid_coords(i, j, matrix):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def get_river_size(x, y, matrix):
    riv_size = 1
    queue = [(x, y)]
    matrix[x][y] = -1
    while queue:
        curr_i, curr_j = queue.pop(0)
        for i in range(len(dx)):
            row, col = curr_i + dx[i], curr_j + dy[i]
            if valid_coords(row, col, matrix) and matrix[row][col] == 1:
                riv_size += 1
                queue.append((row, col))
                matrix[row][col] = -1
    return riv_size


def riverSizes(matrix):
    rivers = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rivers.append(get_river_size(i, j, matrix))
    return rivers


print(riverSizes([[1, 0, 0, 1, 0],
                  [1, 0, 1, 0, 0],
                  [0, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1],
                  [1, 0, 1, 1, 0]]))
