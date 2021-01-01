def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.

    arrayOne.sort()
    arrayTwo.sort()

    first_index = 0
    second_index = 0

    best = float('inf')
    curr = float('inf')
    pair = None

    while first_index < len(arrayOne) and second_index < len(arrayTwo):
        num1 = arrayOne[first_index]
        num2 = arrayTwo[second_index]

        if num1 < num2:
            curr = num2 - num1
            first_index += 1

        elif num2 < num1:
            curr = num1 - num2
            second_index += 1
        else:
            return [num1, num2]

        if best > curr:
            best = curr
            pair = [num1, num2]

    return pair
