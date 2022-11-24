package main

func DFS(graph [][]int, node int, visited []bool, recStack []bool, parent int) bool {
	visited[node] = true
	recStack[node] = true

	for _, adj := range graph[node] {
		if !visited[adj] {
			if DFS(graph, adj, visited, recStack, node) {
				return true
			}
		} else if recStack[adj] {
			return true
		}
	}

	recStack[node] = false
	return false
}

func CycleInGraph(edges [][]int) bool {
	visited := []bool{}
	recStack := []bool{}
	for idx := 0; idx < len(edges); idx++ {
		visited = append(visited, false)
		recStack = append(recStack, false)
	}

	for node := 0; node < len(edges); node++ {
		if !visited[node] {
			if DFS(edges, node, visited, recStack, -1) {
				return true
			}
		}
	}

	return false
}
