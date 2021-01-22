def solve(n, k):
    if n <= k:
        return abs(n - k)
    else:
        return 0 if (k + n) % 2 == 0 else 1


def main():
    n = int(input())
    for _ in range(n):
        n, k = (int(x) for x in input().split(" "))
        print(solve(n, k))


main()
