def matrix_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for row in range(n):
        for col in range(m):
            dp[row + 1][col + 1] = dp[row + 1][col] + \
                dp[row][col + 1] - dp[row][col] + matrix[row][col]

    return dp


def query(i, j, k, l, dp):
    return dp[k + 1][l + 1] - dp[k + 1][j] - dp[i][l + 1] + dp[i][j]


def solve_case(matrix):
    n = len(matrix)
    m = len(matrix[0])
    dp = matrix_sum(matrix)

    res = 0
    for i in range(n):
        for j in range(m):
            for k in range(n):
                for l in range(m):
                    i_l1 = query(i, j, i, l, dp)
                    i_l2 = query(k, l, i, l, dp)
                    if i_l1 >= 2 and i_l2 >= 2 and i_l1 == abs(j - l) + 1 and i_l2 == abs(i - k) + 1:
                        if i_l1 == 2 * i_l2 or i_l2 == 2 * i_l1:
                            res += 1

                    k_j1 = query(i, j, k, j, dp)
                    k_j2 = query(k, l, k, j, dp)
                    if k_j1 >= 2 and k_j2 >= 2 and k_j1 == abs(i - k) + 1 and k_j2 == abs(j - l) + 1:
                        if k_j1 == 2 * k_j2 or k_j2 == 2 * k_j1:
                            res += 1
    return res


T = int(input())
for case in range(T):
    rows, _ = [int(x) for x in input().split()]
    matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    print(f'Case: #{case + 1}: {solve_case(matrix)}')
