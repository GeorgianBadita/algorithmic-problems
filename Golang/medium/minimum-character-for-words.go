package main

func canFormWord(currChars []int, word string) {
	freqWord := []int{}
	for idx := 0; idx < 128; idx++ {
		freqWord = append(freqWord, 0)
	}

	for _, char := range word {
		freqWord[char] += 1
	}

	for idx := 0; idx < 128; idx++ {
		if freqWord[idx] > currChars[idx] {
			currChars[idx] = freqWord[idx]
		}
	}
}

func MinimumCharactersForWords(words []string) []string {
	currChars := []int{}
	for idx := 0; idx < 128; idx++ {
		currChars = append(currChars, 0)
	}

	for _, word := range words {
		canFormWord(currChars, word)
	}

	res := []string{}
	for idx := 0; idx < 128; idx++ {
		cnt := currChars[idx]
		for cnt != 0 {
			res = append(res, string(idx))
			cnt -= 1
		}
	}
	return res
}
