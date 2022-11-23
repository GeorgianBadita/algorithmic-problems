package main

func SunsetViews(buildings []int, direction string) []int {
	if len(buildings) == 0 {
		return []int{}
	}

	if direction == "EAST" {
		res := []int{len(buildings) - 1}
		for idx := len(buildings) - 2; idx >= 0; idx-- {
			last := res[len(res)-1]
			if buildings[idx] > buildings[last] {
				res = append(res, idx)
			}
		}

		for idx := 0; idx < len(res)/2; idx++ {
			res[idx], res[len(res)-idx-1] = res[len(res)-idx-1], res[idx]
		}

		return res

	} else {
		res := []int{0}
		for idx := 1; idx < len(buildings); idx++ {
			last := res[len(res)-1]
			if buildings[idx] > buildings[last] {
				res = append(res, idx)
			}
		}
		return res
	}
}
