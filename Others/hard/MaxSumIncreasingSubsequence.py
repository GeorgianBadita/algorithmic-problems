def maxSumIncreasingSubsequence(array):
    dp = [0] * len(array)
    parent = [None] * len(array)

    dp[0] = array[0]
    for i in range(1, len(array)):
        max_dp = -10**9
        for j in range(0, i):
            if array[j] < array[i] and array[i] + dp[j] > max_dp:
                max_dp = array[i] + dp[j]
                parent[i] = j
        if array[i] > max_dp:
            dp[i] = array[i]
            parent[i] = i
        else:
            dp[i] = max_dp

    max_val = max(dp)
    index = dp.index(max_val)
    if parent[index] is None or parent[index] == index:
        return [max_val, [array[index]]]

    sol = [array[index]]
    while index is not None and parent[index] != index:
        index = parent[index]
        if index is not None:
            sol.insert(0, array[index])

    return [max_val, sol]


arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(maxSumIncreasingSubsequence(arr))
