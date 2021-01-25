def knapsackProblem(items, capacity):

    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    taken = []

    for i in range(1, len(items) + 1):
        for weight in range(0, capacity + 1):
            value, item_weight = items[i - 1]
            if item_weight > weight:
                dp[i][weight] = dp[i - 1][weight]
            else:
                dp[i][weight] = max(dp[i - 1][weight], value + dp[i - 1][weight - item_weight])

    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            taken.insert(0, i - 1)
            j -= items[i - 1][1]
            i -= 1
        if j <= 0:
            break

    return [dp[-1][-1], taken]

print(knapsackProblem(
   [[1, 2], [4, 3], [5, 6], [6, 7]], 10))