def firstDuplicateValue(array):
    seen_set = set()

    for elem in array:
        if elem in seen_set:
            return elem
        seen_set.add(elem)
    return -1
