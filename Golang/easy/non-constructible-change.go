package main

import "sort"

func NonConstructibleChange(coins []int) int {
	if len(coins) == 0 {
		return 1
	}
	sort.Ints(coins)
	minimumChange := 1
	for _, coin := range coins {
		if coin > minimumChange {
			return minimumChange
		}
		minimumChange += coin
	}

	//[5, 7, 1, 1, 3, 22]
	//[1, 1, 2, 3, 5, 7, 22]
	// 0 -> 1 -> 2 -> 5 -> 10 -> 17
	//
	// Write your code here.
	return minimumChange
}
