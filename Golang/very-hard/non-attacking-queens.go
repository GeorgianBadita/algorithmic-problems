package main

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func consistent(sol []int, newCol int) bool {
	if len(sol) == 0 {
		return true
	}

	for row := 0; row <= numRows; row++ {
		if abs(len(sol)-row) == abs(newCol-sol[row]) {
			return false
		}
	}
	return true
}

func generate(n int, sol []int, solCount *int) {
	for col := 0; col < n; col++ {
		if consistent(sol, col) {
			// place kth queen, on row k and col col
			sol = append(sol, col)
			if len(sol) == n {
				*solCount = *solCount + 1
			}
			generate(n, sol, solCount)
			// displace kth queen from row k and col col
			sol = sol[:len(sol)-1]
		}
	}
}

func NonAttackingQueens(n int) int {
	res := 0
	generate(n, []int{}, &res)
	return res
}
