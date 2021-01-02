def spiralTraverse(array):

    num_elements = len(array) * len(array[0])

    n = len(array)
    m = len(array[0])
    it = 0
    result = []
    while num_elements > 0:
        # Up side
        for j in range(it, m - it):
            result.append(array[it][j])
            num_elements -= 1
            if num_elements == 0:
                break
        if num_elements == 0:
            continue

        # Right side
        for i in range(it + 1, n - it):
            result.append(array[i][m - 1 - it])
            num_elements -= 1
            if num_elements == 0:
                break
        if num_elements == 0:
            continue

        # Bottom side
        for j in reversed(range(it, m - 1 - it)):
            result.append(array[n - it - 1][j])
            num_elements -= 1
            if num_elements == 0:
                break
        if num_elements == 0:
            continue

        # Left side
        for i in reversed(range(it + 1, n - it - 1)):
            result.append(array[i][it])
            num_elements -= 1
            if num_elements == 0:
                break
        it += 1

    return result
