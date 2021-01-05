def longestPalindromicSubstring(string):
    if len(string) < 2:
        return string

    max_pal = ''

    for i in range(1, len(string) - 1):
        if string[i] == string[i - 1]:
            pal = check_even_size_pal(i - 1, string)
            if len(pal) > len(max_pal):
                max_pal = pal

        if i == len(string) - 2 and string[i] == string[i + 1]:
            pal = check_even_size_pal(i, string)
            if len(pal) > len(max_pal):
                max_pal = pal

        if string[i - 1] == string[i + 1]:
            pal = check_odd_size_pal(i, string)
            if len(pal) > len(max_pal):
                max_pal = pal

    return max_pal


def check_even_size_pal(poz, arr):
    current_size = 1
    while poz - current_size + 1 >= 0 and poz + current_size < len(arr) and arr[poz - current_size + 1] == arr[poz + current_size]:
        current_size += 1

    return arr[poz - current_size + 2 if poz - current_size + 2 >= 0 else 0: poz + current_size if poz + current_size < len(arr) else None]


def check_odd_size_pal(poz, arr):
    current_size = 1
    while poz - current_size >= 0 and poz + current_size < len(arr) and arr[poz - current_size] == arr[poz + current_size]:
        current_size += 1

    return arr[poz - current_size + 1 if poz - current_size + 1 >= 0 else 0: poz + current_size if poz + current_size < len(arr) else None]


print(longestPalindromicSubstring('abcaa'))
