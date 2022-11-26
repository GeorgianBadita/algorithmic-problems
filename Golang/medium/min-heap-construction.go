package main

import "fmt"

// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
type MinHeap []int

func NewMinHeap(array []int) *MinHeap {
	// Do not edit the lines below.
	heap := MinHeap(array)
	ptr := &heap
	ptr.BuildHeap(array)
	return ptr
}

func (h *MinHeap) BuildHeap(array []int) {
	lastLeaf := (len(array) - 2) / 2
	for idx := lastLeaf + 1; idx >= 0; idx-- {
		h.siftDown(idx)
	}
}

func (h *MinHeap) siftDown(currentIndex int) {
	left := 2*currentIndex + 1
	right := 2*currentIndex + 2
	smallest := currentIndex

	if left < len(*h) && (*h)[smallest] > (*h)[left] {
		smallest = left
	}

	if right < len(*h) && (*h)[smallest] > (*h)[right] {
		smallest = right
	}

	if smallest != currentIndex {
		(*h)[smallest], (*h)[currentIndex] = (*h)[currentIndex], (*h)[smallest]
		h.siftDown(smallest)
	}
}

func (h *MinHeap) siftUp(currentIndex int) {
	parent := (currentIndex - 1) / 2
	if (*h)[parent] > (*h)[currentIndex] {
		(*h)[parent], (*h)[currentIndex] = (*h)[currentIndex], (*h)[parent]
		h.siftUp(parent)
	}
}

func (h MinHeap) Peek() int {
	// Write your code here.
	if len(h) == 0 {
		return -1
	}
	return h[0]
}

func (h *MinHeap) Remove() int {
	if len(*h) == 0 {
		return -1
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
	return peek
}

func (h *MinHeap) Insert(value int) {
	*h = append(*h, value)
	h.siftUp(len(*h) - 1)
}

func main() {
	arr := []int{48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41}
	h := NewMinHeap(arr)
	fmt.Printf("Heap: %v\n", h)
}
