package main

import (
	"sort"
)

type Pair struct {
	first, second int
}

func twoNumberSum(array []int, left int, right int, target int) []Pair {
	result := []Pair{}
	for left < right {
		if array[left]+array[right] == target {
			result = append(result, Pair{array[left], array[right]})
			left += 1
			right -= 1
			for left < len(array)-1 && array[left] == array[left+1] {
				left += 1
			}
			for right > 0 && array[right] == array[right-1] {
				right -= 1
			}
		} else if array[left]+array[right] > target {
			right -= 1
		} else {
			left += 1
		}
	}
	return result
}

func ThreeNumberSum(array []int, target int) [][]int {
	sort.Ints(array)

	res := [][]int{}

	for idx, elem := range array {
		targetSum := target - elem
		sols := twoNumberSum(array, idx+1, len(array)-1, targetSum)

		for _, sol := range sols {
			currSol := []int{elem, sol.first, sol.second}
			res = append(res, currSol)
		}
	}
	return res
}
