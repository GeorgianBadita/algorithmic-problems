package main

import "sort"

func canMerge(int1 []int, int2 []int) bool {
	return int2[0] <= int1[1]
}

func merge(int1 []int, int2 []int) []int {
	second := int2[1]
	if int1[1] > second {
		second = int1[1]
	}
	return []int{int1[0], second}
}

func MergeOverlappingIntervals(intervals [][]int) [][]int {
	if len(intervals) < 2 {
		return intervals
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] < intervals[j][0] {
			return true
		} else if intervals[i][0] > intervals[j][0] {
			return false
		}
		return intervals[i][1] <= intervals[j][1]
	})

	currInt := intervals[0]
	sol := [][]int{}

	for idx := 1; idx < len(intervals); idx += 1 {
		if canMerge(currInt, intervals[idx]) {
			currInt = merge(currInt, intervals[idx])
		} else {
			sol = append(sol, currInt)
			currInt = intervals[idx]
		}
	}
	return append(sol, currInt)
}
