
def minimumWaitingTime(queries):
    queries = sorted(queries)

    for i in range(1, len(queries) - 1):
        queries[i] += queries[i - 1]

    return sum(queries[:-1])


print(minimumWaitingTime([3, 2, 1, 2, 6]))
