package main

import "fmt"

func RunLengthEncoding(str string) string {
	newStr := ""
	currLength := 1
	currChar := str[0]

	for idx := 1; idx < len(str); idx += 1 {
		if str[idx] == currChar {
			currLength += 1
		} else {
			groups := currLength / 9
			lastGroup := currLength % 9
			for gr := 0; gr < groups; gr += 1 {
				newStr = newStr + string('9') + string(currChar)
			}
			if lastGroup > 0 {
				newStr = newStr + fmt.Sprint(lastGroup) + string(currChar)
			}
			currLength = 1
			currChar = str[idx]
		}
	}

	groups := currLength / 9
	lastGroup := currLength % 9
	for gr := 0; gr < groups; gr += 1 {
		newStr = newStr + string('9') + string(currChar)
	}
	if lastGroup > 0 {
		newStr = newStr + fmt.Sprint(lastGroup) + string(currChar)
	}

	return newStr
}
