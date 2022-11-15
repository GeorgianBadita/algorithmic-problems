package main

type BinaryTree struct {
	Value int

	Left  *BinaryTree
	Right *BinaryTree
}

func (tree *BinaryTree) InvertBinaryTree() {
	if tree == nil {
		return
	}
	if tree.Left != nil {
		tree.Left.InvertBinaryTree()
	}

	if tree.Right != nil {
		tree.Right.InvertBinaryTree()
	}

	tree.Left, tree.Right = tree.Right, tree.Left
}
