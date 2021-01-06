def largestRange(array):

    freq = {}

    for num in array:
        freq[num] = True

    max_length = 0
    start = 0

    for num in array:
        if not freq[num]:
            continue

        freq[num] = False
        left = num - 1
        right = num + 1
        length = 1

        while left in freq:
            freq[left] = False
            length += 1
            left -= 1

        while right in freq:
            freq[right] = False
            right += 1
            length += 1

        if length > max_length:
            max_length = length
            start = left + 1

    return [start, start + max_length - 1]


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
