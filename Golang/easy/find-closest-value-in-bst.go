package main

type BST struct {
	Value int

	Left  *BST
	Right *BST
}

func absInt(val int) int {
	if val < 0 {
		return -val
	}
	return val
}

func (tree *BST) Solve(target int, closest int) int {
	if absInt(target-closest) > absInt(target-tree.Value) {
		closest = tree.Value
	}
	if target < tree.Value && tree.Left != nil {
		return tree.Left.Solve(target, closest)
	} else if target >= tree.Value && tree.Right != nil {
		return tree.Right.Solve(target, closest)
	}
	return closest
}

func (tree *BST) FindClosestValue(target int) int {
	return tree.Solve(target, tree.Value)
}

func main() {
}
