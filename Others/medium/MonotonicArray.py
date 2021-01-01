def isMonotonic(array):

    if not array or len(array) == 1:
        return True

    return monotonic(False, array) or monotonic(True, array)


def monotonic(increasing, array):
    if increasing:
        # check for increasing monotonic
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                return False
    else:
        # check for decreasing monotonic
        for i in range(1, len(array)):
            if array[i - 1] < array[i]:
                return False
    return True
