package main

func Solve(array []int, left int, right int) *BST {
	// [1, 2, 5, 7, 10, 13, 14, 15, 22]
	// l = 0, r = 8, m = 3, root = 10, lft = [1, 2, 5, 7], [13, 14, 15, 22]
	if right < left {
		return nil
	}

	if left == right {
		return &BST{Value: array[left]}
	}
	if left < right && left == right-1 {
		return &BST{Value: array[left], Right: &BST{Value: array[right]}}
	}

	mid := left + (right-left)/2
	return &BST{Value: array[mid], Left: Solve(array, left, mid-1), Right: Solve(array, mid+1, right)}
}

func MinHeightBST(array []int) *BST {
	return Solve(array, 0, len(array)-1)
}

type BST struct {
	Value int

	Left  *BST
	Right *BST
}
