def main():
    _ = int(input())

    file_name = input()
    to_del = 0
    current_x_in_row = 0
    for char in file_name:
        if char == 'x':
            current_x_in_row += 1
        else:
            if current_x_in_row >= 3:
                to_del += current_x_in_row - 2
            current_x_in_row = 0
    print(to_del if current_x_in_row < 3 else to_del + current_x_in_row - 2)


main()
