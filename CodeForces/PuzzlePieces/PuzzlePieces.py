def solve(n, m):
    return n == 1 or m == 1 or (n == 2 and m == 2)


def main():
    t = int(input())

    for _ in range(t):
        n, m = (int(x) for x in input().split(' '))

        print("YES" if solve(n, m) else "NO")


main()
