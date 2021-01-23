def get_max(array):
    max_ = array[0]
    pos = 0
    for i in range(len(array)):
        if array[i] > max_:
            max_ = array[i]
            pos = i
    return max_, pos


def get_min_higher_than(array, higher=float('-inf'), higher_pos=float('-inf')):
    min_ = float('inf')
    min_pos = -1

    for i in range(len(array)):
        if array[i] < min_ and array[i] >= higher and i != higher_pos:
            min_ = array[i]
            min_pos = i
    return min_, min_pos


def solve(array, d):
    max_, max_pos = get_max(array)

    if max_ <= d:
        return "YES"

    array_min, min_pos = get_min_higher_than(array)
    array_second_min, min_second_pos = get_min_higher_than(
        array, array_min, higher_pos=min_pos)

    if max_pos != min_pos != min_second_pos and array_min + array_second_min <= d:
        return "YES"
    return "NO"


def main():
    t = int(input())
    for _ in range(t):
        __, d = (int(x) for x in input().split(' '))
        array = [int(x) for x in input().split(' ')]
        print(solve(array, d))


main()
