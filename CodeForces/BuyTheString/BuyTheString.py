def solve(string, c0, c1, h):
    zeros = string.count('0')
    ones = string.count('1')

    if c0 == c1:
        return c0*len(string)

    if h > c0 and h > c1:
        return c0 * zeros + c1 * ones

    total_cost = 0
    if c0 > c1 and h + c1 < c0:
        ones += zeros
        total_cost += zeros * h
        zeros = 0
    elif c1 > c0 and h + c0 < c1:
        zeros += ones
        total_cost += ones * h
        ones = 0

    return total_cost + zeros * c0 + ones * c1


def main():
    t = int(input())

    for _ in range(t):
        __, c0, c1, h = (int(x) for x in input().split(' '))

        string = input()
        print(solve(string, c0, c1, h))


main()
