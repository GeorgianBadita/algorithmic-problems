package main

func consistent(sol []int, candidate int, numTags int) bool {
	// 0 - (
	// 1 - )
	if len(sol) == 0 && candidate == 0 {
		return true
	}

	cnt0 := 0
	cnt1 := 0

	for _, el := range sol {
		if el == 0 {
			cnt0++
		} else {
			cnt1++
		}
	}

	if candidate == 0 {
		cnt0++
	} else {
		cnt1++
	}

	return cnt0 >= cnt1 && cnt0 <= numTags && cnt1 <= numTags
}

func generate(numTags int, sol []int, sols *[]string) {
	for idx := 0; idx <= 1; idx++ {
		if consistent(sol, idx, numTags) {
			sol = append(sol, idx)
			if len(sol) == 2*numTags {
				strSol := ""
				for _, el := range sol {
					if el == 0 {
						strSol += "<div>"
					} else {
						strSol += "</div>"
					}
				}
				*sols = append(*sols, strSol)
			}
			generate(numTags, sol, sols)
			sol = sol[:len(sol)-1]
		}
	}
}

func GenerateDivTags(numberOfTags int) []string {
	sols := []string{}
	generate(numberOfTags, []int{}, &sols)
	return sols
}
