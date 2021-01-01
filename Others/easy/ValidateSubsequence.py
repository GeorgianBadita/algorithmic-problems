def isValidSubsequence(array, sequence):

    if sequence == array or (len(sequence) == 1 and sequence[0] in array) or sequence == array:
        return True

    for elem in array:
        if sequence and elem == sequence[0]:
            sequence.pop(0)

    return len(sequence) == 0


print(isValidSubsequence(
    [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10]))
