package main

func LongestSubstringWithoutDuplication(str string) string {
	dct := map[byte]int{}
	start := 0
	maxSize := 0
	size := 0

	idx := 0
	for idx < len(str) {
		if _, ok := dct[str[idx]]; !ok {
			size++
			dct[str[idx]] = idx
			idx++
		} else {
			if size > maxSize {
				maxSize = size
				start = idx - size
			}
			size = 0
			idx = dct[str[idx]] + 1
			dct = map[byte]int{}
		}
	}

	if size > maxSize {
		start = idx - size
		maxSize = size
	}

	return str[start : start+maxSize]
}
