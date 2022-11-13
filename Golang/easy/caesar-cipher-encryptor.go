package main

func CaesarCipherEncryptor(str string, key int) string {
	runes := []rune(str)
	for idx, char := range runes {
		finalPos := rune('a') + (rune(char-'a')+rune(key))%26
		runes[idx] = finalPos
	}

	return string(runes)
}
