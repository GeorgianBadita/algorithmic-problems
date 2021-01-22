def main():
    power = int(input())

    if power == 0:
        return 1

    if (power - 1) % 4 == 0:
        return 8

    if (power - 1) % 4 == 1:
        return 4

    if (power - 1) % 4 == 2:
        return 2

    return 6


print(main())
