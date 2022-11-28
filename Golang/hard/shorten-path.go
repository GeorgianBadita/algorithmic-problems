package main

import "strings"

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

func filterSlice(slice []string, filterFunc func(string) bool) []string {
	n := 0
	for _, val := range slice {
		if filterFunc(val) {
			slice[n] = val
			n++
		}
	}
	return slice[:n]
}

func ShortenPath(path string) string {
	isFullPath := path[0] == '/'
	pathParts := filterSlice(strings.Split(path, "/"), func(part string) bool { return len(part) > 0 && part != "." })

	stack := Stack{}

	if isFullPath {
		stack.Push("")
	}

	for idx := 0; idx < len(pathParts); idx++ {
		if pathParts[idx] == ".." {
			if stack.IsEmpty() || stack.Peek().(string) == ".." {
				stack.Push(pathParts[idx])
			} else if stack.Peek().(string) != "" {
				stack.Pop()
			}
		} else {
			stack.Push(pathParts[idx])
		}
	}

	if len(stack) == 1 && stack.Peek().(string) == "" {
		return "/"
	}

	pathParts = []string{}
	for !stack.IsEmpty() {
		pathParts = append([]string{stack.Pop().(string)}, pathParts...)
	}

	join := strings.Join(pathParts, "/")

	return join
}
