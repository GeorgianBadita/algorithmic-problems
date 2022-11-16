package main

func MaxSubsetSumNoAdjacent(array []int) int {
	// dp[i] - max subset sum no adj in first i elements
	// dp[0] = a[0], dp[1] = max(dp[0], a[1])
	// dp[i] = max(dp[i - 2] + a[i], dp[i - 1])

	if len(array) == 0 {
		return 0
	}

	if len(array) == 1 {
		return array[0]
	}

	dp := make([]int, len(array))
	dp[0] = array[0]
	dp[1] = max(dp[0], array[1])

	for idx := 2; idx < len(array); idx++ {
		dp[idx] = max(dp[idx-2]+array[idx], dp[idx-1])
	}

	return dp[len(array)-1]
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}
