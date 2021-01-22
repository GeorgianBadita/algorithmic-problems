def main():
    word = input()

    print(''.join([word[0] if ord('A') <= ord(word[0]) <= ord(
        'Z') else chr(ord(word[0]) - (ord('a') - ord('A')))] + list(word[1:])))


main()
