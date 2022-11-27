package main

func ValidStartingCity(distances []int, fuel []int, mpg int) int {
	bestNeg := 0
	bestStIdx := 0
	currSum := 0

	for idx := 0; idx < len(distances); idx++ {
		currSum += fuel[idx]*mpg - distances[idx]
		if currSum < bestNeg {
			bestNeg = currSum
			bestStIdx = (idx + 1) % len(distances)
		}
	}
	return bestStIdx
}
