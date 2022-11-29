package main

var (
	dx []int = []int{-1, 1, 0, 0, -1, 1, -1, 1}
	dy []int = []int{0, 0, -1, 1, -1, 1, 1, -1}
)

// i - 1, j
// i + 1, j
// i, j - 1
// i, j + 1
// i - 1, j - 1
// i + 1, j + 1,
// i - 1, j + 1
// i + 1, j - 1

func validCoords(board [][]rune, i, j int) bool {
	return i >= 0 && i < len(board) && j >= 0 && j < len(board[0])
}

func findWord(board [][]rune, i, j int, word string) bool {
	if word == "" {
		return true
	}
	if board[i][j] != rune(word[0]) {
		return false
	}

	val := board[i][j]
	board[i][j] = '*'

	wordExists := false
	for idx := 0; idx < len(dx); idx++ {
		newI := i + dx[idx]
		newJ := j + dy[idx]
		if validCoords(board, newI, newJ) {
			wordExists = wordExists || findWord(board, newI, newJ, word[1:])
		}
	}
	board[i][j] = val
	return wordExists
}

func BoggleBoard(board [][]rune, words []string) []string {
	res := []string{}
	for _, word := range words {
		currSz := len(res)
		for idx := 0; idx < len(board); idx++ {
			for jdx := 0; jdx < len(board[0]); jdx++ {
				if board[idx][jdx] == rune(word[0]) && findWord(board, idx, jdx, word) {
					res = append(res, word)
					break
				}
			}
			if len(res) > currSz {
				break
			}
		}
	}
	return res
}
