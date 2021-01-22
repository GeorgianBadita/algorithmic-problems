def main():
    n = int(input())
    cnt = 0

    for i in range(n):
        if sum([int(x) for x in input().split(' ')]) >= 2:
            cnt += 1

    print(cnt)


main()
