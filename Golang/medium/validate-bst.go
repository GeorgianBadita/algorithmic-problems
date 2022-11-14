package main

import "math"

type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func validateBST(tree *BST, maxVal, minVal int) bool {
	if tree == nil {
		return true
	}

	currNodeIsBst := tree.Value < maxVal && tree.Value >= minVal

	return validateBST(tree.Left, tree.Value, minVal) && currNodeIsBst && validateBST(tree.Right, maxVal, tree.Value)
}

func (tree *BST) ValidateBst() bool {
	return validateBST(tree, math.MaxInt32, math.MinInt32)
}
