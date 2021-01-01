def findThreeLargestNumbers(array):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')

    for elem in array:
        if elem > max1:
            max3 = max2
            max2 = max1
            max1 = elem
        elif elem > max2:
            max3 = max2
            max2 = elem
        elif elem > max3:
            max3 = elem

    return [max3, max2, max1]
