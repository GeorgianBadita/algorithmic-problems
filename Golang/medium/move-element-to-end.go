package main

func MoveElementToEnd(array []int, toMove int) []int {
	if len(array) == 0 {
		return array
	}

	lastElemPtr := len(array) - 1
	for lastElemPtr >= 0 && array[lastElemPtr] == toMove {
		lastElemPtr -= 1
	}

	if lastElemPtr <= 0 {
		return array
	}

	for idx := 0; idx < lastElemPtr; idx += 1 {
		if array[idx] == toMove {
			tmp := array[idx]
			array[idx] = array[lastElemPtr]
			array[lastElemPtr] = tmp
			for lastElemPtr >= 0 && array[lastElemPtr] == toMove {
				lastElemPtr -= 1
			}
			if lastElemPtr <= 0 {
				break
			}
		}
	}
	return array
}
