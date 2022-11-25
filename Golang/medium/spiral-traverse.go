package main

func SpiralTraverse(array [][]int) []int {
	numElements := len(array) * len(array[0])

	n := len(array)
	m := len(array[0])
	it := 0
	result := []int{}

	for numElements > 0 {
		for j := it; j < m-it; j++ {
			result = append(result, array[it][j])
			numElements -= 1
			if numElements == 0 {
				break
			}
		}

		if numElements == 0 {
			continue
		}

		for i := it + 1; i < n-it; i++ {
			result = apappend(result, array[i][m-1-it])
		}
	}
}
