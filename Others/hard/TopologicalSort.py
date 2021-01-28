def make_graph(jobs, deps):
    graph = {id: [] for id in jobs}

    for dep in deps:
        graph[dep[0]].append(dep[1])
    return graph


def topologicalSort(jobs, deps):
    in_degree = {id: 0 for id in jobs}

    for dep in deps:
        in_degree[dep[1]] += 1

    queue = [x for x in in_degree if in_degree[x] == 0]
    result = []
    graph = make_graph(jobs, deps)

    while queue:
        current_node = queue.pop(0)

        result.append(current_node)

        for adj in graph[current_node]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                queue.append(adj)

    return result if len(result) == len(jobs) else []
