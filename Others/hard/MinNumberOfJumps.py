# O(n^2)
def minNumberOfJumps(array):
    dp = [0] * len(array)
    for i in range(1, len(array)):
        min_val = 10**9
        for j in range(0, i):
            if j + array[j] >= i:
                min_val = min(min_val, dp[j])
        dp[i] = 1 + min_val
    return dp[-1]


# O(n)
def minNumberOfJumps1(array):
    if len(array) <= 2:
        return 0

    curr_coverage, last_jmp_index = 0, 0
    num_jump = 0

    for i in range(len(array)):
        curr_coverage = max(curr_coverage, i + array[i])

        if last_jmp_index == i:
            num_jump += 1
            last_jmp_index = curr_coverage

        if last_jmp_index >= len(array) - 1:
            return num_jump
    return num_jump
