package main

// This is an input class. Do not edit.
type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func heightBalancedBinaryTree(tree *BinaryTree) (int, bool) {
	if tree == nil {
		return 0, true
	}

	leftH, balancedL := heightBalancedBinaryTree(tree.Left)
	rightH, balancedR := heightBalancedBinaryTree(tree.Right)

	return 1 + max(leftH, rightH), balancedL && abs(leftH-rightH) <= 1 && balancedR
}

func HeightBalancedBinaryTree(tree *BinaryTree) bool {
	_, res := heightBalancedBinaryTree(tree)
	return res
}
