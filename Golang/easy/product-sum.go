package main

type SpecialArray []interface{}

func Solve(array []interface{}, depth int) int {
	res := 0

	for _, elem := range array {
		if cast, ok := elem.(SpecialArray); ok {
			res += Solve(cast, depth+1)
		} else {
			res += elem.(int)
		}
	}

	return res * depth
}

// Tip: Each element of `array` can either be cast
// to `SpecialArray` or `int`.
func ProductSum(array []interface{}) int {
	return Solve(array, 1)
}
