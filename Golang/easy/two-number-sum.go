package main

func TwoNumberSum(array []int, target int) []int {
	seen := make(map[int]bool)
	result := make([]int, 2)

	for _, number := range array {
		if _, ok := seen[target-number]; ok {
			result[0] = number
			result[1] = target - number
			return result
		}
		seen[number] = true
	}

	return make([]int, 0)
}

func main() {
}
