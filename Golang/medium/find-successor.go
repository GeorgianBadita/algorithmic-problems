package main

// This is an input class. Do not edit.
type BinaryTree struct {
	Value int

	Left   *BinaryTree
	Right  *BinaryTree
	Parent *BinaryTree
}

func FindSuccessor(tree *BinaryTree, node *BinaryTree) *BinaryTree {
	if node.Right != nil {
		return findLeftMost(node.Right)
	}

	return findRightMostParent(node)
}

func findLeftMost(node *BinaryTree) *BinaryTree {
	for node.Left != nil {
		node = node.Left
	}
	return node
}

func findRightMostParent(node *BinaryTree) *BinaryTree {
	for node.Parent != nil && node.Parent.Right == node {
		node = node.Parent
	}

	return node.Parent
}
