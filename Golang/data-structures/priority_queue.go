package main

// Interface that has to be implemented by elements of the priority queue
// a.CompareWith(b) means, < 0 a has priority over b, = 0, both have the same priority, > 0, b has priority over a
type ElementWithPriority interface {
	CompareWith(ElementWithPriority) int
}

type PriorityQueue []ElementWithPriority

func NewPriorityQueue() *PriorityQueue {
	return &PriorityQueue{}
}

func NewPriorityQueueFromArray(array []ElementWithPriority) *PriorityQueue {
	// Do not edit the lines below.
	heap := PriorityQueue(array)
	ptr := &heap
	ptr.BuildHeap(array)
	return ptr
}

func (h *PriorityQueue) BuildHeap(array []ElementWithPriority) {
	lastLeaf := (len(array) - 2) / 2
	for idx := lastLeaf + 1; idx >= 0; idx-- {
		h.siftDown(idx)
	}
}

func (h *PriorityQueue) siftDown(currentIndex int) {
	left := 2*currentIndex + 1
	right := 2*currentIndex + 2
	smallest := currentIndex

	if left < len(*h) && (*h)[smallest].CompareWith((*h)[left]) > 0 {
		smallest = left
	}

	if right < len(*h) && (*h)[smallest].CompareWith((*h)[right]) > 0 {
		smallest = right
	}

	if smallest != currentIndex {
		(*h)[smallest], (*h)[currentIndex] = (*h)[currentIndex], (*h)[smallest]
		h.siftDown(smallest)
	}
}

func (h *PriorityQueue) siftUp(currentIndex int) {
	parent := (currentIndex - 1) / 2
	if (*h)[parent].CompareWith((*h)[currentIndex]) > 0 {
		(*h)[parent], (*h)[currentIndex] = (*h)[currentIndex], (*h)[parent]
		h.siftUp(parent)
	}
}

func (h PriorityQueue) Peek() *ElementWithPriority {
	// Write your code here.
	if len(h) == 0 {
		return nil
	}
	return &h[0]
}

func (h *PriorityQueue) Remove() *ElementWithPriority {
	if len(*h) == 0 {
		return nil
	}

	if len(*h) == 1 {
		peek := (*h)[0]
		*h = []ElementWithPriority{}
		return &peek
	}

	// Get the minimum element
	peek := (*h)[0]
	// Get the last element of the heap
	lastElem := (*h)[len(*h)-1]
	// Remove it
	*h = (*h)[:len(*h)-1]
	// Put the last element as root
	(*h)[0] = lastElem
	// Sift down
	h.siftDown(0)
	return &peek
}

func (h *PriorityQueue) Insert(value ElementWithPriority) {
	*h = append(*h, value)
	h.siftUp(len(*h) - 1)
}
