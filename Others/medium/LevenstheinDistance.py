def levenshteinDistance(str1, str2):

    if not str1:
        return len(str2)

    if not str2:
        return len(str1)

    dp = [[0] * len(str1) for _ in range(len(str2))]

    inc = 0
    for i in range(len(str1)):
        if str1[i] != str2[0]:
            inc += 1

        dp[0][i] = inc

    inc = 0
    for i in range(len(str2)):
        if str2[i] != str1[0]:
            inc += 1
        dp[i][0] = inc

    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str2[i] == str1[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                   dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
