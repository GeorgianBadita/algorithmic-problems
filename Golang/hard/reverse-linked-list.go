package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func ReverseLinkedList(head *LinkedList) *LinkedList {
	var last *LinkedList

	last = nil

	for head != nil {
		tmp := head.Next
		head.Next = last
		last = head
		head = tmp
	}

	return last
}
