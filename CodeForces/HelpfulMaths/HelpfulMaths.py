def main():
    expression = input()
    ones = 0
    twos = 0
    thrids = 0
    for elem in expression:
        if elem == '1':
            ones += 1
        elif elem == '2':
            twos += 1
        elif elem == '3':
            thrids += 1

    print('+'.join(['1']*ones + ['2']*twos + ['3']*thrids))


main()
