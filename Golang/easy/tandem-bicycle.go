package main

import "sort"

func tandemMax(arr1 []int, arr2 []int, fastest bool) int {
	makeIdx := func(fastest bool, idx int) int {
		if fastest {
			return len(arr2) - idx - 1
		} else {
			return idx
		}
	}

	sum := 0
	for idx := range arr1 {
		valArr1 := arr1[idx]
		valArr2 := arr2[makeIdx(fastest, idx)]

		if valArr1 > valArr2 {
			sum += valArr1
		} else {
			sum += valArr2
		}
	}

	return sum
}

func TandemBicycle(redShirtSpeeds []int, blueShirtSpeeds []int, fastest bool) int {
	sort.Ints(redShirtSpeeds)
	sort.Ints(blueShirtSpeeds)

	if len(redShirtSpeeds) == 0 {
		return 0
	}

	return tandemMax(redShirtSpeeds, blueShirtSpeeds, fastest)
}
