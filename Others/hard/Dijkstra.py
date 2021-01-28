import heapq


def dijkstrasAlgorithm(start, edges):
    dist = [float('inf') for _ in range(len(edges))]

    dist[start] = 0
    queue = [(dist[start], start)]

    while queue:
        current_best_dist, current_node = heapq.heappop(queue)

        if current_best_dist != dist[current_node]:
            continue

        for node in edges[current_node]:
            adj, adj_dist = node[0], node[1]
            if dist[adj] > dist[current_node] + adj_dist:
                dist[adj] = dist[current_node] + adj_dist
                heapq.heappush(queue, (dist[adj], adj))

    return [x if x != float('inf') else -1 for x in dist]
