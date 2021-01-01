def moveElementToEnd(array, toMove):

    pointer = len(array) - 1

    for i in range(len(array) - 1, -1, -1):
        if array[i] == toMove:
            array[i], array[pointer] = array[pointer], array[i]
            pointer -= 1

    return array
