package main

func IsValidSubsequence(array []int, sequence []int) bool {
	if len(array) == 0 && len(sequence) == 0 {
		return true
	}

	idxInSeq := 0
	for _, elem := range array {
		if idxInSeq == len(sequence) {
			return true
		}
		if elem == sequence[idxInSeq] {
			idxInSeq += 1
		}
	}
	return idxInSeq == len(sequence) || false
}

func main() {
}
