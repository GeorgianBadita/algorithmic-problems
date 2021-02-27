def numberOfWaysToTraverseGraph(width, height):
    dp = [[0] * width for _ in range(height)]

    dp[0] = [1] * width
    for i in range(height):
        dp[i][0] = 1

    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
