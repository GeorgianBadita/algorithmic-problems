def compute_goodness(string):
    n = len(string)
    return sum([1 if string[i] != string[n - i - 1] else 0 for i in range(n // 2)])


def solve_case(string, goodness):
    current_goodness = compute_goodness(string)
    return abs(goodness - current_goodness)


T = int(input())
for case in range(T):
    _, K = [int(x) for x in input().split()]
    string = input()
    print(f'Case #{case + 1}: {solve_case(string, K)}')
