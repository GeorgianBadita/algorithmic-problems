package main

// Do not edit the class below except
// for the breadthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
type Node struct {
	Name     string
	Children []*Node
}

type Queue []*Node

func (q *Queue) Push(elem *Node) {
	*q = append(*q, elem)
}

func (q *Queue) Pop() *Node {
	if len(*q) == 0 {
		panic("Trying to pop from empty queue")
	}
	val := (*q)[0]
	*q = (*q)[1:]
	return val
}

func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}

func (n *Node) BreadthFirstSearch(array []string) []string {
	queue := Queue{n}

	for !queue.IsEmpty() {
		node := queue.Pop()
		array = append(array, node.Name)
		for _, child := range node.Children {
			queue.Push(child)
		}
	}

	return array
}
