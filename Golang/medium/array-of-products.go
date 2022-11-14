package main

func ArrayOfProducts(array []int) []int {
	//[5, 1, 4, 2]
	// left: [1, 5, 5, 20]
	// right:[8 ,8, 2, 1]

	left := []int{1}
	for idx := 0; idx < len(array)-1; idx += 1 {
		left = append(left, left[len(left)-1]*array[idx])
	}

	right := []int{1}
	for idx := len(array) - 1; idx > 0; idx-- {
		right = append(right, right[len(right)-1]*array[idx])
	}

	response := []int{}
	for idx := 0; idx < len(array); idx++ {
		response = append(response, left[idx]*right[len(right)-idx-1])
	}
	return response
}
