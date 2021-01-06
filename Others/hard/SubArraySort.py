# O(n) - time | O(1)
def subarraySort(array):
    minimum = float('inf')
    maximum = float('-inf')

    fl = False

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            fl = True
        if fl:
            minimum = min(minimum, array[i])

    fl = False
    for i in range(len(array) - 2, -1, -1):
        if array[i] > array[i + 1]:
            fl = True
        if fl:
            maximum = max(maximum, array[i])

    for l in range(len(array)):
        if array[l] > minimum:
            break

    for r in range(len(array) - 1, -1, -1):
        if array[r] < maximum:
            break

    return [l, r] if r - l > 0 else [-1, -1]
