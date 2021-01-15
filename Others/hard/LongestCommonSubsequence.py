def longestCommonSubsequence(str1, str2):
    if not str1 or not str2:
        return []

    dp = [[0 for _ in range(len(str2))] for __ in range(len(str1))]
    commons = []
    inc = 0
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            inc = 1
        dp[i][0] = inc

    inc = 0
    for j in range(len(str2)):
        if str2[j] == str1[0]:
            inc = 1
        dp[0][j] = inc

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    row = len(str1) - 1
    col = len(str2) - 1

    while row >= 0 and col >= 0:
        if col - 1 >= 0 and dp[row][col] == dp[row][col - 1]:
            col -= 1
        elif row - 1 >= 0 and dp[row][col] == dp[row - 1][col]:
            row -= 1
        else:
            if str1[row] == str2[col]:
                commons.insert(0, str1[row])
            row -= 1
            col -= 1

    return commons
