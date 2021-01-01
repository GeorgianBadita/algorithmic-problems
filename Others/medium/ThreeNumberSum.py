def threeNumberSum(array, targetSum):
    sols = []
    array.sort()
    for i in range(len(array)):
        target = targetSum - array[i]
        for sol in two_sum(array, target, i):
            sols.append([array[i]] + sol)

    return sols


def two_sum(array, target, curr_index):
    solutions = []

    left = curr_index + 1
    right = len(array) - 1

    while left < right:

        if array[left] + array[right] == target:
            solutions.append([array[left], array[right]])
            left += 1
            right -= 1
            while array[left] == array[left - 1]:
                left += 1
            while array[right] == array[right + 1]:
                right -= 1

        elif array[left] + array[right] < target:
            left += 1
        else:
            right -= 1

    return solutions


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
