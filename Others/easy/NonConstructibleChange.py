def bsrch(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


def nonConstructibleChange(coins):
    if not coins:
        return 1

    coins.sort()

    current_target = 0

    for coin in coins:
        if coin > current_target + 1:
            return current_target + 1

        current_target += coin

    return current_target + 1
