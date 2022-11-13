package main

func FirstNonRepeatingCharacter(str string) int {
	occ := make(map[rune]int)
	runes := []rune(str)

	for _, char := range runes {
		occ[char] += 1
	}

	for idx, char := range runes {
		if occ[char] == 1 {
			return idx
		}
	}
	return -1
}
