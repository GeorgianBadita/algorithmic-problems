def process_letter(letter):
    if letter in 'aeiouyAEIOUY':
        return None

    if ord('A') <= ord(letter) <= ord('Z'):
        return chr(ord(letter) + ord('a') - ord('A'))

    return letter


def main():
    string = input()
    new_string = []
    for letter in string:
        procesed_letter = process_letter(letter)
        if procesed_letter:
            new_string.append(f".{procesed_letter}")

    print("".join(new_string))


main()
