def longestPeak(array):

    max_size = 0
    i = 1

    while i < len(array) - 1:
        peak = array[i - 1] < array[i] > array[i + 1]

        if not peak:
            i += 1
            continue

        left = i - 1
        right = i + 1

        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        max_size = max(max_size, right - left - 1)
        i = right

    return max_size
