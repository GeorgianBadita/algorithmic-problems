def bubbleSort(array):

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        current = 1

        for i in range(len(array) - current):
            if array[i] > array[i + 1]:
                is_sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]

        current += 1

    return array
