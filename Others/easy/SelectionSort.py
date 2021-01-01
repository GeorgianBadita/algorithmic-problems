def selectionSort(array):
    current_pos = 0

    while current_pos < len(array):
        aux = current_pos
        for i in range(current_pos, len(array)):
            if array[aux] > array[i]:
                aux = i

        array[aux], array[current_pos] = array[current_pos], array[aux]

        current_pos += 1

    return array
