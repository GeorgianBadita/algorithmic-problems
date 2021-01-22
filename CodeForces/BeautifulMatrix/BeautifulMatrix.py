def main():
    line = 0
    col = 0

    mid_line = 2
    mid_col = 2

    for i in range(5):
        matrix_line = [int(x) for x in input().split(' ')]
        try:
            col = matrix_line.index(1)
            line = i
            break
        except ValueError:
            continue

    print(abs(line - mid_line) + abs(col - mid_col))


main()
