def solve(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return 2 * (abs(b - c) - 2) if (abs(b - c) - 2) > 0 else 0
    if b == c:
        return 2 * (abs(a - b) - 2) if (abs(a - b) - 2) > 0 else 0
    if a == c:
        return 2 * (abs(c - b) - 2) if (abs(c - b) - 2) > 0 else 0

    min_, mid_, max_ = sorted([a, b, c])
    return abs(min_ - mid_) - 1 + abs(min_ - max_) - 1 + abs(max_ - mid_) - 2


def main():
    q = int(input())

    for _ in range(q):
        a, b, c = (int(x) for x in input().split(' '))

        print(solve(a, b, c))


main()
