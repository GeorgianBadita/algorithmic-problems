def numberOfWaysToMakeChange(n, denoms):
    dp = [0]*(n+1)
    dp[0] = 1

    for denom in denoms:
        for i in range(1, n + 1):
            if i - denom >= 0:
                dp[i] += dp[i - denom]

    return dp[n]


print(numberOfWaysToMakeChange(6, [1, 5]))
