package main

func TournamentWinner(competitions [][]string, results []int) string {
	scores := make(map[string]int)
	bestScore := 0
	bestLang := ""
	for idx, competition := range competitions {
		key := competition[1-results[idx]]
		scores[key] += 3
		if scores[key] > bestScore {
			bestScore = scores[key]
			bestLang = key
		}
	}
	return bestLang
}
