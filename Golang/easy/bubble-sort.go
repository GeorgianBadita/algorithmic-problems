package main

func BubbleSort(array []int) []int {
	sorted := false
	currIter := 1
	for !sorted {
		sorted = true
		for idx := 0; idx < len(array)-currIter; idx += 1 {
			if array[idx] > array[idx+1] {
				sorted = false
				tmp := array[idx]
				array[idx] = array[idx+1]
				array[idx+1] = tmp
			}
		}
		currIter += 1
	}
	return array
}
