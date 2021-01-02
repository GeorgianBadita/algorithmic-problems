def maxSubsetSumNoAdjacent(array):
    # Write your code here.

    if not array:
        return 0

    if len(array) < 3:
        return max(array)

    dp = [0]*len(array)

    dp[0] = array[0]
    dp[1] = max(array[1], dp[0])

    for i in range(2, len(array)):
        dp[i] = max(dp[i - 1], array[i] + dp[i - 2])

    return max(dp)
