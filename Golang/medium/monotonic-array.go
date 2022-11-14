package main

func compare(idx int, arr []int, firstCmpIdx int) bool {
	if arr[firstCmpIdx] < arr[firstCmpIdx+1] {
		return arr[idx] <= arr[idx+1]
	}
	return arr[idx] >= arr[idx+1]
}

func IsMonotonic(array []int) bool {
	if len(array) <= 1 {
		return true
	}

	firstComparableIdx := 0
	for firstComparableIdx < len(array)-1 && array[firstComparableIdx] == array[firstComparableIdx+1] {
		firstComparableIdx += 1
	}

	if firstComparableIdx == len(array)-1 {
		return true
	}

	for idx := 0; idx < len(array)-1; idx++ {
		if !compare(idx, array, firstComparableIdx) {
			return false
		}
	}
	return true
}
