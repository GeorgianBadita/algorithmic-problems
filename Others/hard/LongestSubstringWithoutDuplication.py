def longestSubstringWithoutDuplication(string):
    if not string or len(string) == 1:
        return string

    current_length = 1
    max_length = 1
    max_length_start = 0
    seen = {string[0]: 0}

    i = 1
    while i < len(string):
        if string[i] not in seen:
            seen[string[i]] = i
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_length_start = i - max_length

            i = seen[string[i]]
            seen = {}
            current_length = 0
        i += 1
    if current_length > max_length:
        max_length = current_length
        max_length_start = i - max_length

    return string if current_length == len(string) else string[max_length_start: max_length_start + max_length]


print(longestSubstringWithoutDuplication("abcbde"))
