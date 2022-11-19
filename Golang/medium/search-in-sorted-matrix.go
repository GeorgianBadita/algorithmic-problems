package main

func SearchInSortedMatrix(matrix [][]int, target int) []int {
	rowStart := len(matrix) - 1
	colStart := 0

	for colStart < len(matrix[0]) && rowStart >= 0 {
		if matrix[rowStart][colStart] == target {
			return []int{rowStart, colStart}
		}
		if matrix[rowStart][colStart] > target {
			rowStart -= 1
		} else {
			colStart += 1
		}
	}

	return []int{-1, -1}
}
