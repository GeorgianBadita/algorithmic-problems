package main

import "math"

func MinNumberOfCoinsForChange(n int, denoms []int) int {
	dp := make([]int, n+1)
	for idx := 0; idx <= n; idx++ {
		dp[idx] = math.MaxInt16
	}

	for _, denom := range denoms {
		if denom <= n {
			dp[denom] = 1
		}
	}
	dp[0] = 0

	for _, denom := range denoms {
		for idx := 1; idx <= n; idx++ {
			if idx-denom >= 0 && 1+dp[idx-denom] < dp[idx] {
				dp[idx] = 1 + dp[idx-denom]
			}
		}
	}

	if dp[n] == math.MaxInt16 {
		return -1
	}
	return dp[n]
}
