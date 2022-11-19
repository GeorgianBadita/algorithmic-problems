package main

var mapping = map[rune][]rune{
	'1': {'1'},
	'2': {'a', 'b', 'c'},
	'3': {'d', 'e', 'f'},
	'4': {'g', 'h', 'i'},
	'5': {'j', 'k', 'l'},
	'6': {'m', 'n', 'o'},
	'7': {'p', 'q', 'r', 's'},
	'8': {'t', 'u', 'v'},
	'9': {'w', 'x', 'y', 'z'},
	'0': {'0'},
}

func generateMnemonics(phoneNumber string, sol []rune, sols *[]string) {
	if len(sol) >= len(phoneNumber) {
		return
	}
	for _, value := range mapping[int32(phoneNumber[len(sol)])] {
		if len(sol) < len(phoneNumber) {
			sol = append(sol, value)
			if len(sol) == len(phoneNumber) {
				*sols = append(*sols, string(sol))
			}
			generateMnemonics(phoneNumber, sol, sols)
			sol = sol[:len(sol)-1]
		}
	}
}

func PhoneNumberMnemonics(phoneNumber string) []string {
	sols := []string{}
	generateMnemonics(phoneNumber, []rune{}, &sols)
	return sols
}
