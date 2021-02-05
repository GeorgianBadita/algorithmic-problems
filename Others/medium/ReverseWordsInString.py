def reverseWordsInString(string):
    # Write your code here.

    if not string or len(string) == 1:
        return string

    current_word = ""
    current_word_pos = len(string) - 1
    result = []

    while current_word_pos >= 0:
        if string[current_word_pos] != ' ':
            current_word = string[current_word_pos] + current_word
            current_word_pos -= 1
        else:
            while current_word_pos >= 0 and string[current_word_pos] == ' ':
                current_word += " "
                current_word_pos -= 1
            result.append(current_word)
            current_word = ""

    if current_word:
        result.append(current_word)

    return ''.join(result)
