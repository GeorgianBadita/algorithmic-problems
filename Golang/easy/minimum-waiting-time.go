package main

import "sort"

func MinimumWaitingTime(queries []int) int {
	sort.Ints(queries)
	sum := 0
	sumSoFar := 0

	for _, elem := range queries[:len(queries)-1] {
		sumSoFar += elem
		sum += sumSoFar
	}

	return sum
}
