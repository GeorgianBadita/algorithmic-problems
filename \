package main

func KadanesAlgorithm(array []int) int {
	if len(array) == 0 {
		return 0
	}

	if len(array) == 1 {
		return array[0]
	}

	s := array[0]
	maxS := array[0]

	for idx := 1; idx < len(array); idx++ {
		if s < 0 {
			s = 0
		}
		s += array[idx]
		if s > maxS {
			maxS = s
		}
	}
	return maxS
}
