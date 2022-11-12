package main

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func RemoveDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {
	if linkedList.Next == nil {
		return linkedList
	}

	uniqueHead := linkedList
	toRet := uniqueHead
	beforeList := linkedList
	linkedList = linkedList.Next
	for linkedList != nil {
		if beforeList.Value != linkedList.Value {
			uniqueHead.Value = beforeList.Value
			uniqueHead = uniqueHead.Next
		}
		beforeList = beforeList.Next
		linkedList = linkedList.Next
	}

	uniqueHead.Value = beforeList.Value
	uniqueHead.Next = nil
	return toRet
}
