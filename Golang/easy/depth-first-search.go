package main

// ================ MY OWN STACK IMPLEMENTATION ======================

type Stack []*Node

func (s Stack) Push(v *Node) Stack {
	return append(s, v)
}

func (s Stack) Pop() (Stack, *Node) {
	length := len(s)
	if length == 0 {
		panic("Trying to pop from empty stack!")
	}
	return s[:length-1], s[length-1]
}

func (s Stack) IsEmpty() bool {
	return len(s) == 0
}

// ===================================================================

// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
type Node struct {
	Name     string
	Children []*Node
}

func (n *Node) DepthFirstSearch(array []string) []string {
	stack := Stack{n}
	var elem interface{}
	for !stack.IsEmpty() {
		stack, elem = stack.Pop()
		node := elem.(*Node)
		array = append(array, node.Name)
		for idx := len(node.Children) - 1; idx >= 0; idx-- {
			stack = stack.Push(node.Children[idx])
		}
	}
	return array
}
