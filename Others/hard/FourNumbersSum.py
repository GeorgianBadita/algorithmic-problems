def fourNumberSum(array, targetSum):
    sums = {}

    quads = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            target = targetSum - (array[i] + array[j])
            if target in sums:
                for x, y in sums[target]:
                    quads.append([array[i], array[j], x, y])

        for k in range(0, i):
            if array[i] + array[k] not in sums:
                sums[array[i] + array[k]] = [(array[i], array[k])]
            else:
                sums[array[i] + array[k]].append((array[i], array[k]))

    return quads
