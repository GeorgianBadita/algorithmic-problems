package main

import "math"

// This is an input class. Do not edit.
type BST struct {
	Value int

	Left  *BST
	Right *BST
}

type Info struct {
	rootIdx int
}

func makeBST(preOrder []int, min, max int, info *Info) *BST {
	if info.rootIdx == len(preOrder) {
		return nil
	}

	rootVal := preOrder[info.rootIdx]
	if rootVal < min || rootVal >= max {
		return nil
	}

	info.rootIdx += 1
	return &BST{Value: rootVal, Left: makeBST(preOrder, min, rootVal, info), Right: makeBST(preOrder, rootVal, max, info)}
}

func ReconstructBst(preOrderTraversalValues []int) *BST {
	return makeBST(preOrderTraversalValues, math.MinInt32, math.MaxInt32, &Info{rootIdx: 0})
}
