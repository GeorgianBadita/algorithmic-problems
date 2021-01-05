def balancedBrackets(string):

    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for bracket in string:
        if bracket not in list(brackets.keys()) + list(brackets.values()):
            continue
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            if not stack or brackets[bracket] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0
