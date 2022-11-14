package main

import (
	"math"
	"sort"
)

func SmallestDifference(array1, array2 []int) []int {
	sort.Ints(array1)
	sort.Ints(array2)

	smallest, current := math.MaxInt32, math.MaxInt32
	smallestPair := []int{}
	idx1, idx2 := 0, 0

	for idx1 < len(array1) && idx2 < len(array2) {
		first, second := array1[idx1], array2[idx2]

		if first < second {
			current = second - first
			idx1 += 1
		} else if first > second {
			current = first - second
			idx2 += 1
		} else {
			return []int{first, second}
		}

		if current < smallest {
			smallest = current
			smallestPair = []int{first, second}
		}
	}
	return smallestPair
}
