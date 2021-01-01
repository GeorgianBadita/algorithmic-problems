def runLengthEncoding(string):
    curr_mult = 1

    new_str = []
    for i in range(len(string) - 1):
        if string[i] != string[i + 1] or curr_mult == 9:
            new_str.append(str(curr_mult) + string[i])
            curr_mult = 1
        else:
            curr_mult += 1

    return ''.join(new_str + [str(curr_mult) + string[-1]])
