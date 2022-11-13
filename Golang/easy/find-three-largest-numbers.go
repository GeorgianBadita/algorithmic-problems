package main

import "fmt"

func max(elems ...int) int {
	if len(elems) == 0 {
		panic("Cannot compute maximum with 0 elements")
	}

	maxEl := elems[0]

	for idx := range elems {
		if elems[idx] > maxEl {
			maxEl = elems[idx]
		}
	}
	return maxEl
}

func min(elems ...int) int {
	if len(elems) == 0 {
		panic("Cannot compute minimum with 0 elements")
	}

	minEl := elems[0]

	for idx := range elems {
		if elems[idx] < minEl {
			minEl = elems[idx]
		}
	}
	return minEl
}

func FindThreeLargestNumbers(array []int) []int {
	var max1, max2, max3 int
	max1 = max(array[0], array[1], array[2])
	max3 = min(array[0], array[1], array[2])
	max2 = array[0] + array[1] + array[2] - max1 - max3

	for idx := 3; idx < len(array); idx += 1 {
		fmt.Printf("Max3 = %v, Max2 = %v, Max1 = %v, curr el = %v\n\n", max3, max2, max1, array[idx])
		if array[idx] >= max1 {
			max3 = max2
			max2 = max1
			max1 = array[idx]
		} else if array[idx] >= max2 {
			max3 = max2
			max2 = array[idx]
		} else if array[idx] >= max3 {
			max3 = array[idx]
		}
	}
	return []int{max3, max2, max1}
}

func main() {
	arr := []int{7, 8, 3, 11, 43, 55}
	fmt.Print(FindThreeLargestNumbers(arr))
}
