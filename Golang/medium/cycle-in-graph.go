package main

type Queue []int

func (q *Queue) Enqueue(elem int) {
	*q = append(*q, elem)
}

func (q *Queue) Dequeue() int {
	if len(*q) == 0 {
		panic("Dequeuing from empty queue")
	}
	ret := (*q)[0]
	*q = (*q)[1:]
	return ret
}

func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}

type Set map[int]bool

func (mp *Set) Exists(elem int) bool {
	_, ok := (*mp)[elem]
	return ok
}

func bfs(graph [][]int, start int) bool {
	queue := Queue{start}
	visited := Set{}
	visited[start] = true
	parent := []int{}

	for idx := 0; idx < len(graph); idx++ {
		parent = append(parent, -1)
	}

	parent[start] = start

	for !queue.IsEmpty() {
		currNode := queue.Dequeue()
		for _, adj := range graph[currNode] {
			if visited.Exists(adj) && parent[adj] != parent[currNode] {
				return true
			}

			if !visited.Exists(adj) {
				visited[adj] = true
				parent[adj] = currNode
				queue.Enqueue(adj)

			}
		}
	}
	return false
}

func CycleInGraph(edges [][]int) bool {
	if len(edges) == 0 {
		return false
	}
	return bfs(edges, 0)
}
