package main

func ThreeNumberSort(array []int, order []int) []int {
	if len(array) < 2 {
		return array
	}

	firstPtr := 0
	lastPtr := len(array) - 1
	firstVal := order[0]
	lastVal := order[2]

	for idx := firstPtr; idx <= lastPtr; idx++ {
		val := array[idx]
		if val == firstVal {
			array[firstPtr], array[idx] = array[idx], array[firstPtr]
			firstPtr++
		} else if val == lastVal {
			array[lastPtr], array[idx] = array[idx], array[lastPtr]
			lastPtr--
			idx--
		}
	}

	return array
}
