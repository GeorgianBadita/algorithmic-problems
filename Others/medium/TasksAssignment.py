def taskAssignment(k, tasks):
    if len(tasks) == 2:
        return [[0, 1]]

    indexes = [i for i in range(len(tasks))]
    indexes = sorted(indexes, key=lambda x: tasks[x])    

    return [[indexes[i], indexes[len(tasks) - i - 1]] for i in range(len(indexes) // 2)]