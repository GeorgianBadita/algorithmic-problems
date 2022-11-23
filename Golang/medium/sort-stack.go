package main

type Stack []int

func (s *Stack) Push(elem int) {
	*s = append(*s, elem)
}

func (s *Stack) Pop() int {
	if len(*s) == 0 {
		panic("")
	}
	elem := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return elem
}

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Peek() int {
	if len(*s) == 0 {
		panic("")
	}
	elem := (*s)[len(*s)-1]
	return elem
}

func (s *Stack) Sort() {
	if len(*s) <= 1 {
		return
	}

	elem := s.Pop()
	s.Sort()

	tmpStack := Stack{}
	for !s.IsEmpty() && elem < s.Peek() {
		tmpStack.Push(s.Pop())
	}
	s.Push(elem)
	for !tmpStack.IsEmpty() {
		s.Push(tmpStack.Pop())
	}
}

func SortStack(stack []int) []int {
	st := Stack{}
	for idx := len(stack) - 1; idx >= 0; idx-- {
		st.Push(stack[idx])
	}

	st.Sort()
	// Write your code here.
	return st
}
