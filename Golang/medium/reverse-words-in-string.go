package main

type Stack []string

func (s *Stack) Push(str string) {
	*s = append(*s, str)
}

func (s *Stack) Pop() string {
	elem := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return elem
}

func ReverseWordsInString(str string) string {
	word := ""
	ws := ""
	stack := Stack{}

	for _, char := range str {
		if char != ' ' {
			if len(ws) > 0 {
				stack.Push(ws)
				ws = ""
			}
			word += string(char)
		} else {
			if len(word) > 0 {
				stack.Push(word)
				word = ""
			}
			ws += string(char)
		}
	}

	if len(ws) > 0 {
		stack.Push(ws)
	}
	if len(word) > 0 {
		stack.Push(word)
	}

	res := ""
	for len(stack) != 0 {
		curr := stack.Pop()
		res += curr
	}
	return res
}
