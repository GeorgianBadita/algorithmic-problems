package main

type Node struct {
	Value      int
	Prev, Next *Node
}

type DoublyLinkedList struct {
	Head, Tail *Node
}

func NewDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (ll *DoublyLinkedList) SetHead(node *Node) {
	if ll == nil {
		*ll = *NewDoublyLinkedList()
		ll.Head = node
		ll.Tail = node
		ll.Head.Prev = nil
		ll.Tail.Next = nil
	} else {
		if ll.Head == nil {
			ll.Head = node
			ll.Tail = node
			ll.Head.Prev = nil
			ll.Tail.Next = nil
		} else {
			if node == ll.Tail {
				ll.Tail = ll.Tail.Prev
			}
			ll.removeBindings(node)
			ll.Head.Prev = node
			node.Next = ll.Head
			ll.Head = node
			ll.Head.Prev = nil
		}
	}
}

func (ll *DoublyLinkedList) SetTail(node *Node) {
	if ll == nil {
		*ll = *NewDoublyLinkedList()
		ll.Head = node
		ll.Tail = node
		ll.Head.Prev = nil
		ll.Tail.Next = nil
	} else {
		if ll.Head == node {
			nd := ll.Head
			ll.Head = ll.Head.Next
			ll.Head.Prev = nil
			ll.Tail.Next = nd
			nd.Prev = ll.Tail
			ll.Tail = ll.Tail.Next
			ll.Tail.Next = nil
		} else if ll.Tail == nil {
			ll.SetHead(node)
		} else {
			ll.removeBindings(node)
			ll.Tail.Next = node
			node.Prev = ll.Tail
			ll.Tail = node
			ll.Tail.Next = nil
		}
	}
}

func (ll *DoublyLinkedList) InsertBefore(node, nodeToInsert *Node) {
	if node == ll.Head {
		ll.SetHead(nodeToInsert)
		return
	}

	ll.removeBindings(nodeToInsert)
	prevNode := node.Prev
	nodeToInsert.Next = node
	node.Prev = nodeToInsert
	prevNode.Next = nodeToInsert
	nodeToInsert.Prev = prevNode
}

func (ll *DoublyLinkedList) InsertAfter(node, nodeToInsert *Node) {
	if node == ll.Tail {
		ll.SetTail(nodeToInsert)
		return
	}
	ll.InsertAfter(node.Next, nodeToInsert)
}

func (ll *DoublyLinkedList) InsertAtPosition(position int, nodeToInsert *Node) {
	if position == 1 {
		ll.SetHead(nodeToInsert)
		return
	}
	node := ll.Head
	currPos := 1
	for node != nil && currPos != position {
		node = node.Next
		currPos += 1
	}
	if node != nil {
		ll.InsertBefore(node, nodeToInsert)
	} else {
		ll.SetTail(nodeToInsert)
	}
}

func (ll *DoublyLinkedList) RemoveNodesWithValue(value int) {
	head := ll.Head
	for head != nil {
		nodeToRemove := head
		head = head.Next
		if nodeToRemove.Value == value {
			ll.Remove(nodeToRemove)
		}
	}
}

func (ll *DoublyLinkedList) Remove(node *Node) {
	if node == ll.Head {
		ll.Head = ll.Head.Next
	}
	if node == ll.Tail {
		ll.Tail = ll.Tail.Prev
	}

	ll.removeBindings(node)
}

func (ll *DoublyLinkedList) ContainsNodeWithValue(value int) bool {
	head := ll.Head
	for head != nil {
		if head.Value == value {
			return true
		}
		head = head.Next
	}
	return false
}

func (ll *DoublyLinkedList) removeBindings(node *Node) {
	if node.Prev != nil {
		node.Prev.Next = node.Next
	}
	if node.Next != nil {
		node.Next.Prev = node.Prev
	}
	node.Prev = nil
	node.Next = nil
}
