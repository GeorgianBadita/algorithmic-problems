def solve(array):

    even = []
    odd = []

    for i in range(len(array)):
        if array[i] % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if even:
        return f"1\n{even[-1] + 1}"

    if len(odd) > 1:
        return f"2\n{odd[-1] + 1} {odd[-2] + 1}"
    else:
        return "-1"


def main():
    t = int(input())

    for _ in range(t):
        __ = int(input())

        array = [int(x) for x in input().split(' ')]

        print(solve(array))


main()
