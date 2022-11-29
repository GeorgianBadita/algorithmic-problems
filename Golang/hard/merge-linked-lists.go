package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func makeK(k int, ll *LinkedList) int {
	size := 0
	for ll != nil {
		size++
		ll = ll.Next
	}
	isNeg := k < 0
	if isNeg {
		k *= -1
	}

	mod := k % size
	if mod == 0 {
		return 0
	}

	if isNeg {
		return size - mod
	}
	return mod
}

func ShiftLinkedList(head *LinkedList, k int) *LinkedList {
	k = makeK(k, head)

	if k == 0 {
		return head
	}

	firstPtr := head
	for k > 0 {
		firstPtr = firstPtr.Next
		k--
	}

	secondPtr := head
	for firstPtr.Next != nil {
		firstPtr = firstPtr.Next
		secondPtr = secondPtr.Next
	}

	ret := secondPtr.Next
	secondPtr.Next = nil
	firstPtr.Next = head
	return ret
}
