def sortedSquaredArray(array):
    smallest = 0
    largest = len(array) - 1

    result = []
    while smallest <= largest:
        if abs(array[smallest]) > abs(array[largest]):
            val = array[smallest]
            smallest += 1
        else:
            val = array[largest]
            largest -= 1
        result.append(val*val)
    return list(reversed(result))


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
