def main():
    num_words = int(input())

    for _ in range(num_words):
        current_word = input()
        if len(current_word) > 10:
            print(
                f"{current_word[0]}{len(current_word) - 2}{current_word[-1]}")
        else:
            print(current_word)


main()
