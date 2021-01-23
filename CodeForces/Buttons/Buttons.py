def main():
    num_buttons = int(input())
    print(num_buttons + (num_buttons**2)*(num_buttons + 1)//2 -
          (num_buttons)*(num_buttons + 1)*(2*num_buttons + 1) // 6)


main()
