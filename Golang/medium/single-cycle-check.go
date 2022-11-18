package main

import "math"

func HasSyngleCycle(array []int) bool {
	numVisited := 0
	currIdx := 0
	for numVisited != len(array) {
		numVisited += 1
		nextIdx := currIdx + array[currIdx]
		if nextIdx >= len(array) {
			nextIdx = nextIdx % len(array)
		} else if nextIdx < 0 {
			if -nextIdx%len(array) == 0 {
				nextIdx = 0
			} else {
				tmp := -nextIdx
				cuant := int(math.Ceil(float64(tmp) / float64(len(array))))
				nextIdx += cuant * len(array)
			}
		}
		if array[currIdx] == 0 {
			return false
		}
		array[currIdx] = 0
		currIdx = nextIdx
	}
	return currIdx == 0
}
