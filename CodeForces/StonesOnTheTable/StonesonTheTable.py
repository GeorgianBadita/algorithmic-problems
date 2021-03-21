def main():
    _ = input()
    string = input()

    if _ == 0 or _ == 1:
        return 0

    if _ == 2:
        if string[0] == string[1]:
            return 1
        return 0

    last = string[0]
    cnt = 0
    for i in range(1, len(string)):
        if string[i] == last:
            cnt += 1
        last = string[i]
    return cnt


print(main())
