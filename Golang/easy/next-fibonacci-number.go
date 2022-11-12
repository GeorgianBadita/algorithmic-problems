package main

func GetNthFib(n int) int {
	if n <= 1 {
		return 0
	}

	first := 0
	second := 1
	third := 1

	for idx := 3; idx <= n; idx += 1 {
		third = first + second
		first = second
		second = third
	}

	return third
}
