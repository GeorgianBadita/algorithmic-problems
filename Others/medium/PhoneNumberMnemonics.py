# https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics


def phoneNumberMnemonics(phoneNumber):
    # Write your code here.

    mapping = {
        '0': '0',
        '1': '1',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    solutions = []

    def get_mnemonics(current_solution):
        if len(current_solution) < len(phoneNumber):
            for candidate in mapping[phoneNumber[len(current_solution)]]:
                current_solution.append(candidate)
                if len(current_solution) == len(phoneNumber):
                    solutions.append(''.join(current_solution))
                get_mnemonics(current_solution)
                current_solution.pop()

    get_mnemonics([])
    return solutions
