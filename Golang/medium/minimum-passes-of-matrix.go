package main

import "fmt"

func validCoords(matrix [][]int, i, j int) bool {
	return i >= 0 && i < len(matrix) && j >= 0 && j < len(matrix[0])
}

type Pair struct {
	x, y int
}

func checkHasNegatives(matrix [][]int) []Pair {
	res := []Pair{}
	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] < 0 {
				res = append(res, Pair{r, c})
			}
		}
	}
	return res
}

func MinimumPassesOfMatrix(matrix [][]int) int {
	passes := 0
	negativePairs := checkHasNegatives(matrix)

	dx := []int{-1, 1, 0, 0}
	dy := []int{0, 0, -1, 1}

	for len(negativePairs) > 0 {
		passes++
		canBeMadePositive := []Pair{}
		for _, pair := range negativePairs {
			for dir := 0; dir < len(dx); dir++ {
				newX := pair.x + dx[dir]
				newY := pair.y + dy[dir]
				if validCoords(matrix, newX, newY) && matrix[newX][newY] > 0 {
					canBeMadePositive = append(canBeMadePositive, Pair{pair.x, pair.y})
					break
				}
			}
		}
		if len(canBeMadePositive) == 0 {
			return -1
		}
		for _, pair := range canBeMadePositive {
			matrix[pair.x][pair.y] *= -1
		}

		negativePairs = checkHasNegatives(matrix)
	}
	return passes
}

func main() {
	matrix := [][]int{
		{0, -1, -3, 2, 0},
		{1, -2, -5, -1, -3},
		{3, 0, 0, -4, -1},
	}

	fmt.Printf("Minimum passes: %v\n", MinimumPassesOfMatrix(matrix))
}
