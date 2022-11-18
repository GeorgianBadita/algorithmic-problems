package main

func validCoords(matrix [][]int, i, j int) bool {
	return i >= 0 && i < len(matrix) && j >= 0 && j < len(matrix[0])
}

var (
	dx []int = []int{-1, 1, 0, 0}
	dy []int = []int{0, 0, -1, 1}
)

func riverSize(matrix [][]int, i, j int) int {
	if matrix[i][j] != 1 {
		return 0
	}
	matrix[i][j] = 0
	res := 0
	for idx := 0; idx < len(dx); idx++ {
		newI := i + dx[idx]
		newJ := j + dy[idx]

		if validCoords(matrix, newI, newJ) && matrix[newI][newJ] == 1 {
			res += 1 + riverSize(matrix, newI, newJ)
		}
	}
	return res
}

func RiverSizes(matrix [][]int) []int {
	res := []int{}
	for idx := 0; idx < len(matrix); idx++ {
		for jdx := 0; jdx < len(matrix[0]); jdx++ {
			if matrix[idx][jdx] == 1 {
				res = append(res, 1+riverSize(matrix, idx, jdx))
			}
		}
	}
	return res
}
