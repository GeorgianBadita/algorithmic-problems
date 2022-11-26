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
			result = append(result, array[i][m-1-it])
			numElements -= 1
			if numElements == 0 {
				break
			}
		}

		if numElements == 0 {
			continue
		}

		for j := m - it - 2; j >= it; j-- {
			result = append(result, array[n-it-1][j])
			numElements -= 1
			if numElements == 0 {
				break
			}
		}

		if numElements == 0 {
			continue
		}

		for i := n - it - 2; i >= it+1; it-- {
			result = append(result, array[i][it])
			numElements -= 1
			if numElements == 0 {
				break
			}
		}

		it += 1
	}
	return result
}
