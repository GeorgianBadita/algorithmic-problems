def perfect_array(length):
    return ' '.join(['1']*length)


def main():
    t = int(input())

    for _ in range(t):
        length = int(input())

        print(perfect_array(length))


main()
