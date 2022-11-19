package main

// This is an input struct. Do not edit.
type LinkedList struct {
	Value int
	Next  *LinkedList
}

func SumOfLinkedLists(linkedListOne *LinkedList, linkedListTwo *LinkedList) *LinkedList {
	res := &LinkedList{}
	toRet := res
	carry := 0
	for linkedListOne != nil && linkedListTwo != nil {
		currVal := linkedListOne.Value + linkedListTwo.Value + carry
		carry = currVal / 10
		currVal %= 10
		res.Next = &LinkedList{Value: currVal}
		res = res.Next
		linkedListOne = linkedListOne.Next
		linkedListTwo = linkedListTwo.Next
	}

	for linkedListOne != nil {
		currVal := linkedListOne.Value + carry
		carry = currVal / 10
		currVal %= 10
		res.Next = &LinkedList{Value: currVal}
		res = res.Next
		linkedListOne = linkedListOne.Next
	}

	for linkedListTwo != nil {
		currVal := linkedListTwo.Value + carry
		carry = currVal / 10
		currVal %= 10
		res.Next = &LinkedList{Value: currVal}
		res = res.Next
		linkedListTwo = linkedListTwo.Next
	}

	if carry != 0 {
		res.Next = &LinkedList{Value: carry}
	}

	return toRet.Next
}
