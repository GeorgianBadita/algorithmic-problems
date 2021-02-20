def dp(height, max_steps, memo):

    if height == 0:
        return 1

    if memo[height] > 0:
        return memo[height]

    ways = 0
    for i in range(max(height - max_steps, 0), height):
        ways += dp(i, max_steps, memo)
    memo[height] = ways
    return ways


def staircaseTraversal(height, maxSteps):
    memo = [-1] * (height + 1)
    dp(height, maxSteps, memo)
    return memo[height]
