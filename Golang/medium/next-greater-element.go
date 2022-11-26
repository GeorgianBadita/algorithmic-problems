package main

func NextGreaterElement(array []int) []int {
	result := make([]int, 0)
	for range array {
		result = append(result, -1)
	}

	stack := make([]int, 0)

	for idx := 2*len(array) - 1; idx >= 0; idx-- {
		cIdx := idx % len(array)
		for len(stack) > 0 {
			if stack[len(stack)-1] <= array[cIdx] {
				stack = stack[:len(stack)-1]
			} else {
				result[cIdx] = stack[len(stack)-1]
				break
			}
		}

		stack = append(stack, array[cIdx])
	}
	return result
}
