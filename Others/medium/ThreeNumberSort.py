def threeNumberSort(array, order):
    zero = order[0]
    two = order[2]

    zero_index = 0
    two_index = len(array) - 1
    current_index = 0

    while current_index <= two_index:
        if array[current_index] == zero:
            array[zero_index], array[current_index] = array[current_index], array[zero_index]
            zero_index += 1
            current_index += 1
        elif array[current_index] == two:
            array[current_index], array[two_index] = array[two_index], array[current_index]
            two_index -= 1
        else:
            current_index += 1

    return array
