package main

type Dep struct {
	Prereq int
	Job    int
}

type Graph map[int][]int

type Queue []int

func (q *Queue) Push(elem int) {
	*q = append(*q, elem)
}

func (q *Queue) Dequeue() int {
	if q.IsEmpty() {
		panic("Dequeuing from an empty queue...")
	}
	toRet := (*q)[0]
	*q = (*q)[1:]
	return toRet
}

func (q Queue) IsEmpty() bool {
	return len(q) == 0
}

func TopologicalSort(jobs []int, deps []Dep) []int {
	graph := Graph{}
	inDeg := map[int]int{}

	for _, job := range jobs {
		inDeg[job] = 0
		graph[job] = []int{}
	}

	for _, dep := range deps {
		inDeg[dep.Job]++
		graph[dep.Prereq] = append(graph[dep.Prereq], dep.Job)
	}

	// TOPO SORT
	queue := Queue{}

	for job, deg := range inDeg {
		if deg == 0 {
			queue.Push(job)
		}
	}

	res := []int{}

	for !queue.IsEmpty() {
		node := queue.Dequeue()
		res = append(res, node)
		for _, adj := range graph[node] {
			inDeg[adj]--
			if inDeg[adj] == 0 {
				queue = append(queue, adj)
			}
		}
	}

	if len(res) != len(jobs) {
		return []int{}
	}
	return res
}
