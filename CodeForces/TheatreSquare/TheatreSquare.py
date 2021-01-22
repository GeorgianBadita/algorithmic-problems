def main():
    n, m, a = (int(x) for x in input().split(' '))
    length = n // a if n % a == 0 else n // a + 1
    height = m // a if m % a == 0 else m // a + 1

    print(length * height)


main()
