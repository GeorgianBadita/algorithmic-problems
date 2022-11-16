package main

import (
	"fmt"
)

func NumberOfWaysToMakeChange(n int, denoms []int) int {
	dp := make([]int, n+1)
	for idx := 0; idx <= n; idx++ {
		dp[idx] = 0
	}
	dp[0] = 1

	for _, denom := range denoms {
		for idx := 1; idx <= n; idx++ {
			if idx-denom >= 0 {
				dp[idx] += dp[idx-denom]
			}
		}
	}
	fmt.Printf("%v\n", dp)
	return dp[n]
}

func main() {
	n := 6
	denoms := []int{1, 5}

	NumberOfWaysToMakeChange(n, denoms)
}
