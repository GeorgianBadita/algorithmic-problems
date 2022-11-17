package main

func LevenshteinDistance(a, b string) int {
	// dp[i][j] - Levenshtein distance between first i chars of a and first j chars of b
	// dp[0][j] = {1, a[0] = b[j] else 0}
	// dp[i][0] = {1, a[i] = b[0] else 0}
	// dp[i][j] = {dp[i - 1][j - 1], a[i] = b[j], 1 + min( min(dp[i - 1][j], dp[i][j - 1]))}

	if a == b {
		return 0
	}

	if len(a) == 0 {
		return len(b)
	}

	if len(b) == 0 {
		return len(a)
	}

	dp := make([][]int, len(a))

	for idx := 0; idx < len(a); idx++ {
		dp[idx] = make([]int, len(b))
		for jdx := 0; jdx < len(b); jdx++ {
			dp[idx][jdx] = 0
		}
	}

	initVal := 0

	for idx := 0; idx < len(a); idx++ {
		if a[idx] != b[0] {
			initVal++
		}
		dp[idx][0] = initVal
	}

	initVal = 0

	for jdx := 0; jdx < len(b); jdx++ {
		if b[jdx] != a[0] {
			initVal += 1
		}
		dp[0][jdx] = initVal
	}

	for idx := 1; idx < len(a); idx++ {
		for jdx := 1; jdx < len(b); jdx++ {
			if a[idx] == b[jdx] {
				dp[idx][jdx] = dp[idx-1][jdx-1]
			} else {
				dp[idx][jdx] = 1 + min(dp[idx-1][jdx], dp[idx][jdx-1], dp[idx-1][jdx-1])
			}
		}
	}

	return dp[len(a)-1][len(b)-1]
}

func min(arg1 int, arg2 int, res ...int) int {
	minVal := arg1

	if arg2 < arg1 {
		minVal = arg2
	}

	for _, value := range res {
		if value < minVal {
			minVal = value
		}
	}
	return minVal
}
