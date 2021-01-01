def is_valid_address(address):
    if address[0] == '.' or address[-1] == '.':
        return False

    groups = address.split('.')
    if len(groups) != 4:
        return False

    for group in groups:
        if group[0] == '0' and len(group) != 1:
            return False

        num = 0
        for dig in group:
            num = num * 10 + int(dig)

        if num < 0 or num > 255:
            return False
    return True


def validIPAddresses(string):
    sols = []

    for i in range(len(string) - 2):
        for j in range(i + 1, len(string) - 1):
            for k in range(j + 1, len(string)):
                current_address = string[:i] + '.' + \
                    string[i:j] + '.' + string[j:k] + '.' + string[k:]
                if is_valid_address(current_address):
                    sols.append(current_address)
    return sols
