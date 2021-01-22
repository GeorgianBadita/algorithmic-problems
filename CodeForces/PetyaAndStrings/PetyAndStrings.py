def get_letter(x):
    if ord('A') <= ord(x) <= ord('Z'):
        return chr(ord(x) + ord('a') - ord('A'))
    return x


def main():
    str1 = input()
    str2 = input()

    i = 0
    while i < len(str1):
        l1 = get_letter(str1[i])
        l2 = get_letter(str2[i])

        if l1 < l2:
            print(-1)
            return

        elif l1 > l2:
            print(1)
            return
        i += 1

    print(0)


main()
