package main

func makeRow(height int) []int {
	row := []int{}
	row = append(row, 1)
	for idx := 0; idx < height-1; idx++ {
		row = append(row, 1)
	}
	return row
}

func NumberOfWaysToTraverseGraph(width int, height int) int {
	if width*height == 0 {
		return 0
	}

	firstRow := make([]int, width)

	for idx := 0; idx < width; idx++ {
		firstRow[idx] = 1
	}

	secondRow := makeRow(width)

	for idx := 1; idx < height; idx++ {
		for jdx := 1; jdx < width; jdx++ {
			secondRow[jdx] = secondRow[jdx-1] + firstRow[jdx]
		}
		firstRow = secondRow
		secondRow = makeRow(width)
	}

	return firstRow[len(firstRow)-1]
}
