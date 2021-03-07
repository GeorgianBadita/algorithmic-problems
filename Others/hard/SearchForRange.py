def first_occurance(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            if mid == 0 or array[mid - 1] != target:
                return mid
            right = mid - 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def last_occurance(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            if mid == len(array) - 1 or array[mid + 1] != target:
                return mid
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def searchForRange(array, target):
    return [first_occurance(array, target), last_occurance(array, target)]


print(searchForRange([5, 7, 7, 8, 8, 10], 5))
