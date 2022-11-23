package main

import "math"

type StackElem struct {
	Value, Min, Max int
}

type Stack []StackElem

func (s *Stack) Push(elem StackElem) {
	*s = append(*s, elem)
}

func (s *Stack) Pop() StackElem {
	if len(*s) == 0 {
		panic("Popping from empty stack...")
	}
	elem := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return elem
}

func (s *Stack) Peek() StackElem {
	if len(*s) == 0 {
		panic("Peeking from empty stack...")
	}
	elem := (*s)[len(*s)-1]
	return elem
}

type MinMaxStack struct {
	stack    Stack
	min, max int
}

func NewMinMaxStack() *MinMaxStack {
	return &MinMaxStack{stack: Stack{}, min: math.MaxInt32, max: math.MinInt32}
}

func (stack *MinMaxStack) Peek() int {
	val := stack.stack.Peek()
	return val.Value
}

func (stack *MinMaxStack) Pop() int {
	ret := stack.stack.Pop()
	if len(stack.stack) > 0 {
		val := stack.stack.Peek()
		if val.Max != stack.max {
			stack.max = val.Max
		}
		if val.Min != stack.min {
			stack.min = val.Min
		}
	}
	return ret.Value
}

func (stack *MinMaxStack) Push(number int) {
	if number > stack.max || len(stack.stack) == 0 {
		stack.max = number
	}
	if number < stack.min || len(stack.stack) == 0 {
		stack.min = number
	}
	stack.stack.Push(StackElem{Value: number, Min: stack.min, Max: stack.max})
}

func (stack *MinMaxStack) GetMin() int {
	return stack.min
}

func (stack *MinMaxStack) GetMax() int {
	return stack.max
}
