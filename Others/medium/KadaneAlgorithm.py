def kadanesAlgorithm(array):
    max_sum = array[0]
    s = array[0]

    for i in range(1, len(array)):
        if s < 0:
            s = 0
        s += array[i]
        if s > max_sum:
            max_sum = s

    return max_sum
