package main

import "strconv"

func partValidation(part string) bool {
	if len(part) == 0 || len(part) > 3 {
		return false
	}

	if len(part) > 1 && part[0] == '0' {
		return false
	}

	if part == "0" {
		return true
	}

	parse, err := strconv.Atoi(part)
	if err != nil {
		return false
	}

	return parse >= 0 && parse <= 255
}

func isValid(first, second, third, fourth string) bool {
	return partValidation(first) && partValidation(second) && partValidation(third) && partValidation(fourth)
}

func ValidIPAddresses(str string) []string {
	res := []string{}

	for idx := 0; idx < len(str)-2; idx++ {
		for jdx := idx + 1; jdx < len(str)-1; jdx++ {
			for kdx := jdx + 1; kdx < len(str); kdx++ {
				firstPart := str[:idx]
				secondPart := str[idx:jdx]
				thirdPart := str[jdx:kdx]
				fourthPart := str[kdx:]

				if isValid(firstPart, secondPart, thirdPart, fourthPart) {
					res = append(res, firstPart+"."+secondPart+"."+thirdPart+"."+fourthPart)
				}
			}
		}
	}
	return res
}
