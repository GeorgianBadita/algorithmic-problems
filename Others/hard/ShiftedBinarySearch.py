def find_shift_point(array):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if mid == len(array) - 1 or (mid < len(array) and array[mid] > array[mid + 1]):
            return mid
        if array[mid] > array[0]:
            left = mid + 1
        else:
            right = mid - 1
    return mid


def bsrch(array, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def shiftedBinarySearch(array, target):
    shitf_pos = find_shift_point(array)
    if shitf_pos == len(array) - 1:
        return bsrch(array, 0, len(array) - 1, target)

    if target >= array[0]:
        return bsrch(array, 0, shitf_pos, target)
    else:
        return bsrch(array, shitf_pos + 1, len(array) - 1, target)


print(shiftedBinarySearch([45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 45))
