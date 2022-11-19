package main

func staircaseTraversal(height int, maxSteps int, memo map[int]int) int {
	if height < 0 {
		return 0
	}
	if height <= 1 {
		return 1
	}
	if val, ok := memo[height]; ok {
		return val
	}
	res := 0

	for idx := 1; idx <= maxSteps; idx++ {
		res += staircaseTraversal(height-idx, maxSteps, memo)
	}

	memo[height] = res
	return res
}

func StaircaseTraversal(height int, maxSteps int) int {
	return staircaseTraversal(height, maxSteps, map[int]int{})
}
