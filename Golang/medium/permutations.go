package main

func generate(array []int, sol []int, solutions *[][]int, used []bool) {
	for idx := 0; idx < len(array); idx++ {
		if !used[idx] {
			sol = append(sol, array[idx])
			used[idx] = true
			if len(sol) == len(array) {
				*solutions = append(*solutions, append([]int{}, sol...))
			}
			generate(array, sol, solutions, used)
			sol = sol[:len(sol)-1]
			used[idx] = false
		}
	}
}

func GetPermutations(array []int) [][]int {
	used := []bool{}
	for idx := 0; idx < len(array); idx++ {
		used = append(used, false)
	}
	sols := [][]int{}

	generate(array, []int{}, &sols, used)
	return sols
}
