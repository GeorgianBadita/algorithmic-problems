package main

func FirstDuplicateValue(array []int) int {
	// [2, 1, 5, 2, 3, 3, 4]
	// [2, 1, -5, ]

	for idx := 0; idx < len(array); idx++ {
		absIdx := array[idx]
		if absIdx < 0 {
			absIdx *= -1
		}

		if array[absIdx-1] < 0 {
			return absIdx
		}

		array[absIdx-1] *= -1
	}
	return -1
}
