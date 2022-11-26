package main

func getPalindromigSubstringLength(str string, pos int) string {
	currPos := pos
	length := 0
	for currPos-length-1 >= 0 && currPos+length+1 < len(str) && str[currPos+length+1] == str[currPos-length-1] {
		length++
	}

	end := currPos + length + 1
	if end > len(str) {
		end = len(str)
	}

	oddPalindrome := str[currPos-length : end]

	length = 0
	currPos = pos
	for currPos-length >= 0 && currPos+length+1 < len(str) && str[currPos-length] == str[currPos+length+1] {
		length++
	}

	end = currPos + length + 1
	if end > len(str) {
		end = len(str)
	}

	evenPalindrome := str[currPos-length+1 : end]

	if len(oddPalindrome) > len(evenPalindrome) {
		return oddPalindrome
	}
	return evenPalindrome
}

func LongestPalindromicSubstring(str string) string {
	if len(str) < 2 {
		return str
	}

	pal := ""

	for idx := 0; idx < len(str); idx++ {
		currPal := getPalindromigSubstringLength(str, idx)
		if len(currPal) > len(pal) {
			pal = currPal
		}
	}
	return pal
}
