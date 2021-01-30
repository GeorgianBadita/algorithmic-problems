def solve(n, k):
    if k == 1 or n == k:
        return 1

    if n < k:
        return int(k / n) if k % n == 0 else int(k / n) + 1
    else:
        c = int(n / k)
        d = n % k
        if d != 0:
            c += 1
        k *= c
        return int(k / n) if k % n == 0 else int(k / n) + 1


def main():
    t = int(input())

    for _ in range(t):
        n, k = (int(x) for x in input().split())

        print(solve(n, k))


main()
