package main

// This is an input class. Do not edit.
type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func FindKthLargestValueInBst(tree *BST, k int) int {
	stack := []*BST{}

	for tree != nil || len(stack) > 0 {
		for tree != nil {
			stack = append(stack, tree)
			tree = tree.Right
		}
		k -= 1
		tree = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if k == 0 {
			return tree.Value
		}
		tree = tree.Left
	}
	return -1
}
