def twoNumberSum(array, targetSum):

    seen_sums = set()
    for elem in array:
        if targetSum - elem in seen_sums:
            return [elem, targetSum - elem]
        seen_sums.add(elem)

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))


def twoNumberSumSort(array, targetSum):
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]

        if array[left] + array[right] < targetSum:
            left += 1
        else:
            right -= 1

    return []
