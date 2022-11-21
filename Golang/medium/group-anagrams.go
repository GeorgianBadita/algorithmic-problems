package main

import "sort"

func GroupAnagrams(words []string) [][]string {
	res := map[string][]string{}

	for _, word := range words {
		toRune := []rune(word)
		sort.Slice(toRune, func(i, j int) bool { return toRune[i] < toRune[j] })
		toString := string(toRune)
		val, ok := res[toString]
		if ok {
			res[toString] = append(val, word)
		} else {
			res[toString] = []string{word}
		}
	}

	values := [][]string{}
	for k := range res {
		values = append(values, res[k])
	}
	return values
}
