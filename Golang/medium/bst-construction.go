package main

// Do not edit the class below except for
// the insert, contains, and remove methods.
// Feel free to add new properties and methods
// to the class.
type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func (tree *BST) Insert(value int) *BST {
	if tree == nil {
		return &BST{Value: value}
	}

	var parent *BST
	root := tree
	for root != nil {
		if value < root.Value {
			parent = root
			root = root.Left
		} else {
			parent = root
			root = root.Right
		}
	}

	if value < parent.Value {
		parent.Left = &BST{Value: value}
	} else {
		parent.Right = &BST{Value: value}
	}

	return tree
}

func (tree *BST) Contains(value int) bool {
	if tree == nil {
		return false
	}

	if tree.Value == value {
		return true
	}

	if value < tree.Value {
		return tree.Left.Contains(value)
	}
	return tree.Right.Contains(value)
}

func (tree *BST) Remove(value int) *BST {
	if tree == nil {
		return tree
	}

	if value < tree.Value {
		tree.Left = tree.Left.Remove(value)
	} else if value > tree.Value {
		tree.Right = tree.Right.Remove(value)
	} else {
		if tree.Left == nil && tree.Right == nil {
			return nil
		}
		if tree.Left != nil && tree.Right == nil {
			tree.Value = tree.Left.Value
			tree.Right = tree.Left.Right
			tree.Left = tree.Left.Left
		} else if tree.Right != nil && tree.Left == nil {
			tree.Value = tree.Right.Value
			tree.Left = tree.Right.Left
			tree.Right = tree.Right.Right
		} else {
			successor := findSuccessor(tree.Right)
			tree.Value = successor
			tree.Right = tree.Right.Remove(successor)
		}
	}
	return tree
}

func findSuccessor(node *BST) int {
	for node.Left != nil {
		node = node.Left
	}
	return node.Value
}
