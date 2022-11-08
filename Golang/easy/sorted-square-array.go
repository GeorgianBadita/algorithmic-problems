package main

func SortedSquaredArray(array []int) []int {
	result := make([]int, len(array))
	idx := len(result) - 1
	start := 0
	end := len(array) - 1

	for ok := true; ok; ok = start <= end {
		startVal := array[start] * array[start]
		endVal := array[end] * array[end]

		if startVal >= endVal {
			start += 1
			result[idx] = startVal
		} else {
			end -= 1
			result[idx] = endVal
		}

		idx -= 1
	}

	return result
}
