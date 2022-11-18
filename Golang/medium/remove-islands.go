package main

func validCoords(matrix [][]int, i, j int) bool {
	return i >= 0 && i < len(matrix) && j >= 0 && j < len(matrix[0])
}

var (
	dx []int = []int{-1, 1, 0, 0}
	dy []int = []int{0, 0, -1, 1}
)

func traverseIsland(matrix [][]int, i, j, mark int) {
	if matrix[i][j] != 1 {
		return
	}
	matrix[i][j] = mark

	for idx := 0; idx < len(dx); idx++ {
		ii := i + dx[idx]
		jj := j + dy[idx]

		if validCoords(matrix, ii, jj) {
			traverseIsland(matrix, ii, jj, mark)
		}
	}
}

func RemoveIslands(matrix [][]int) [][]int {
	for idx := 0; idx < len(matrix); idx++ {
		if matrix[idx][0] == 1 {
			traverseIsland(matrix, idx, 0, 2)
		}
		if matrix[idx][len(matrix[0])-1] == 1 {
			traverseIsland(matrix, idx, len(matrix[0])-1, 2)
		}
	}

	for jdx := 0; jdx < len(matrix[0]); jdx++ {
		if matrix[0][jdx] == 1 {
			traverseIsland(matrix, 0, jdx, 2)
		}
		if matrix[len(matrix)-1][jdx] == 1 {
			traverseIsland(matrix, len(matrix)-1, jdx, 2)
		}
	}

	for idx := 1; idx < len(matrix)-1; idx++ {
		for jdx := 1; jdx < len(matrix[0])-1; jdx++ {
			if matrix[idx][jdx] == 1 {
				traverseIsland(matrix, idx, jdx, 0)
			}
		}
	}

	for idx := 0; idx < len(matrix); idx++ {
		for jdx := 0; jdx < len(matrix[0]); jdx++ {
			if matrix[idx][jdx] == 2 {
				matrix[idx][jdx] = 1
			}
		}
	}

	return matrix
}
