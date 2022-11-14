package main

func LongestPeak(array []int) int {
	// State -> increasing
	// State -> decreasing

	if len(array) < 3 {
		return 0
	}

	currLength := 0
	maxLength := 0
	state := "increasing"

	for idx := 0; idx < len(array)-1; idx++ {
		if state == "increasing" {
			if array[idx] < array[idx+1] {
				currLength += 1
			} else if array[idx] > array[idx+1] && currLength > 0 {
				currLength += 1
				state = "decreasing"
			} else {
				state = "increasing"
				currLength = 0
			}
		} else {
			if array[idx] > array[idx+1] {
				currLength += 1
			} else if currLength > 1 {
				if currLength > maxLength {
					maxLength = currLength
				}
				idx -= 1
				currLength = 0
				state = "increasing"
			}
		}
	}

	if state == "decreasing" && currLength > 1 {
		if currLength > maxLength {
			maxLength = currLength
		}
	}

	if maxLength+1 >= 3 {
		return maxLength + 1
	} else {
		return 0
	}
}
