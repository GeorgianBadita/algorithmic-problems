package main

import "sort"

func isConsistent(sol []int, nextElem int) bool {
	if len(sol) == 0 {
		return true
	}

	return nextElem > sol[len(sol)-1]
}

func generate(array []int, sol []int, solutions *[][]int) {
	for _, elem := range array {
		if isConsistent(sol, elem) {
			sol = append(sol, elem)
			*solutions = append(*solutions, append([]int{}, sol...))
			generate(array, sol, solutions)
			sol = sol[:len(sol)-1]
		}
	}
}

func Powerset(array []int) [][]int {
	sort.Ints(array)
	sols := [][]int{{}}
	generate(array, []int{}, &sols)
	return sols
}
