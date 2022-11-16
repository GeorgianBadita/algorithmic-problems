package main

// This is an input class. Do not edit.
type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func binaryTreeDiameter(tree *BinaryTree) (int, int) {
	if tree == nil {
		return 0, 0
	}

	lHeight, lDiam := binaryTreeDiameter(tree.Left)
	rHeight, rDiam := binaryTreeDiameter(tree.Right)

	return 1 + max(lHeight, rHeight), max(lDiam, max(rDiam, lHeight+rHeight))
}

func BinaryTreeDiameter(tree *BinaryTree) int {
	_, res := binaryTreeDiameter(tree)
	return res
}
