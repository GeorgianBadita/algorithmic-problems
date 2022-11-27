package main

type Element interface{}

type Stack []Element

func (s *Stack) Push(element Element) {
	*s = append(*s, element)
}

func (s *Stack) Pop() Element {
	ret := s.Peek()
	*s = (*s)[:len(*s)-1]
	return ret
}

func (s Stack) Peek() Element {
	if s.IsEmpty() {
		panic("Trying to peek from an empty Stack...")
	}
	return s[len(s)-1]
}

func (s Stack) IsEmpty() bool {
	return len(s) == 0
}
