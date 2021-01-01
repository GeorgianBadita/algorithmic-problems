def getNthFib(n):
    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1

    first = 0
    second = 1
    current_term = None

    for _ in range(2, n):
        current_term = first + second
        first = second
        second = current_term

    return current_term


print(getNthFib(2))
