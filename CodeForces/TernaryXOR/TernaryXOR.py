def solve(ternary_number):
    a = "1"
    b = "1"
    greater = False
    for i in range(1, len(ternary_number)):
        if ternary_number[i] == '0':
            a += '0'
            b += '0'
        else:
            if not greater and ternary_number[i] == '2':
                a += '1'
                b += '1'
            elif greater and ternary_number[i] == '2':
                a += '0'
                b += '2'
            elif not greater and ternary_number[i] == '1':
                a += '1'
                b += '0'
                greater = True
            elif greater and ternary_number[i] == '1':
                a += '0'
                b += '1'

    return a + '\n' + b


def main():
    n = int(input())

    for _ in range(n):
        __ = input()
        ternary_number = input()
        print(solve(ternary_number))


main()
