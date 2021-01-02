def minNumberOfCoinsForChange(n, denoms):

    num_coins = [float('inf') for i in range(n + 1)]

    num_coins[0] = 0

    for denom in denoms:
        for i in range(len(num_coins)):
            if i - denom >= 0:
                num_coins[i] = min(num_coins[i], num_coins[i - denom] + 1)

    return num_coins[n] if num_coins[n] != float('inf') else -1
