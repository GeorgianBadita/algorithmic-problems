package main

func makeFreq(characters string) map[rune]int {
	res := make(map[rune]int)
	runes := []rune(characters)
	for _, char := range runes {
		res[char] += 1
	}

	return res
}

func GenerateDocument(characters string, document string) bool {
	charsFreq := makeFreq(characters)
	docFreq := makeFreq(document)

	for char, occ := range docFreq {
		val, ok := charsFreq[char]
		if !ok || occ > val {
			return false
		}
	}
	return true
}
