def insertionSort(array):
    current_pos = 0

    while current_pos < len(array) - 1:
        i = current_pos
        while array[i + 1] < array[i] and i >= 0:
            array[i + 1], array[i] = array[i], array[i + 1]
            i -= 1
        current_pos += 1

    return array
