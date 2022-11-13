package main

func IsPalindrome(str string) bool {
	for idx := 0; idx < len(str)/2; idx += 1 {
		if str[idx] != str[len(str)-idx-1] {
			return false
		}
	}
	return true
}
