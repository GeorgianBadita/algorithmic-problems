def cycleInGraph(edges):

    in_deg = [0] * len(edges)

    for vertex in edges:
        for adj in edges[vertex]:
            in_deg[adj] += 1

    queue = [x for x in range(len(edges)) if in_deg[x] == 0]

    while queue:
        current_node = queue.pop(0)
        for adj in edges[current_node]:
            in_deg[adj] -= 1
            if in_deg[adj] == 0:
                queue.append(adj)

    return sum(in_deg) == 0
