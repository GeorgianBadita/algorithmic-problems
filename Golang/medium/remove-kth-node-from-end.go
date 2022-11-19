package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func RemoveKthNodeFromEnd(head *LinkedList, k int) {
	//
	// 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
	// k = 1

	startPtr := head
	for k > 0 {
		startPtr = startPtr.Next
		k -= 1
	}

	if startPtr == nil {
		*head = *head.Next
		return
	}

	secondPtr := head
	for startPtr.Next != nil {
		startPtr = startPtr.Next
		secondPtr = secondPtr.Next
	}

	if secondPtr != nil && secondPtr.Next != nil {
		secondPtr.Next = secondPtr.Next.Next
	}
}
