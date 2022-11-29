package main

import "sort"

func twoSum(array []int, left, right, target int) [][]int {
	res := [][]int{}
	for left < right {
		if array[left]+array[right] == target {
			res = append(res, []int{array[left], array[right]})
			left++
			right--
		} else if array[left]+array[right] < target {
			left++
		} else {
			right--
		}
	}
	return res
}

func FourNumberSum(array []int, target int) [][]int {
	sort.Ints(array)
	sol := [][]int{}

	for idx := 0; idx < len(array)-1; idx++ {
		for jdx := idx + 1; jdx < len(array); jdx++ {
			newTraget := target - array[idx] - array[jdx]
			twoSumSol := twoSum(array, jdx+1, len(array)-1, newTraget)
			for _, ts := range twoSumSol {
				sol = append(sol, []int{array[idx], array[jdx], ts[0], ts[1]})
			}
		}
	}
	return sol
}
