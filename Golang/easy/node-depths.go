package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

func Solve(root *BinaryTree, depth int) int {
	if root == nil {
		return 0
	}

	leftRes := Solve(root.Left, depth+1)
	rightRes := Solve(root.Right, depth+1)

	return depth + leftRes + rightRes
}

func NodeDepths(root *BinaryTree) int {
	return Solve(root, 0)
}
