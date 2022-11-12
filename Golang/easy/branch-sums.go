package main

// This is the struct of the input root. Do not edit it.
type BinaryTree struct {
	Value int
	Left  *BinaryTree
	Right *BinaryTree
}

func Solve(root *BinaryTree) []int {
	if root.Left == nil && root.Right == nil {
		return []int{root.Value}
	}
	leftSums := []int{}
	if root.Left != nil {
		leftSums = Solve(root.Left)
	}

	rightSums := []int{}
	if root.Right != nil {
		rightSums = Solve(root.Right)
	}

	for idx := range leftSums {
		leftSums[idx] += root.Value
	}

	for idx := range rightSums {
		rightSums[idx] += root.Value
	}

	return append(leftSums, rightSums...)
}

func BranchSums(root *BinaryTree) []int {
	return Solve(root)
}
