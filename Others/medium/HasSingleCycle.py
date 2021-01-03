#O(n) - time | O(n) - space
def hasSingleCycle(array):
    seen_indexes = set()

    index = 0
    while index not in seen_indexes:
        seen_indexes.add(index)
        next_index = index + array[index]
        if next_index >= len(array):
            next_index = next_index % len(array)
        elif next_index < 0:
            while next_index < 0:
                next_index += len(array)

        index = next_index

    return set([x for x in range(len(array))]) == seen_indexes and index == 0

#O(n) - time | O(1) - space


def hasSingleCycle1(array):
    index = 0

    while array[index] != 'x':
        array_val = array[index]
        array[index] = 'x'
        index += array_val
        if index >= len(array):
            index = index % len(array)
        elif index < 0:
            while index < 0:
                index += len(array)

    return index == 0 and array.count('x') == len(array)


hasSingleCycle1([2, 3, 1, -4, -4, 2])
