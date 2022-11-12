package main

import "sort"

func cmpArrays(arr1 []int, arr2 []int) bool {
	for idx := range arr1 {
		if arr1[idx] <= arr2[idx] {
			return false
		}
	}
	return true
}

func ClassPhotos(redShirtHeights []int, blueShirtHeights []int) bool {
	sort.Ints(redShirtHeights)
	sort.Ints(blueShirtHeights)

	if redShirtHeights[0] > blueShirtHeights[0] {
		return cmpArrays(redShirtHeights, blueShirtHeights)
	} else if redShirtHeights[0] < blueShirtHeights[0] {
		return cmpArrays(blueShirtHeights, redShirtHeights)
	}

	return false
}
