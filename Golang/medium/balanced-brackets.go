package main

type Stack []rune

func (s *Stack) Push(elem rune) {
	*s = append(*s, elem)
}

func (s *Stack) Pop() rune {
	elem := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return elem
}

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func BalancedBrackets(s string) bool {
	brackets := map[rune]rune{
		']': '[',
		')': '(',
		'}': '{',
	}

	allBrackets := []rune{'[', ']', '{', '}', '(', ')'}

	st := Stack{}

	for _, elem := range s {
		// I know I can have a set here but I am too lazy rn
		contains := false
		for _, br := range allBrackets {
			if br == elem {
				contains = true
				break
			}
		}
		if !contains {
			continue
		}
		val, closed := brackets[elem]
		if !closed {
			st.Push(elem)
		} else {
			if st.IsEmpty() {
				return false
			}
			top := st.Pop()
			if top != val {
				return false
			}
		}
	}

	return st.IsEmpty()
}
