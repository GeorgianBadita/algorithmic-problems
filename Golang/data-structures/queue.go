package main

type Element interface{}

type Queue []Element

func (q *Queue) Enqueue(element Element) {
	*q = append(*q, element)
}

func (q *Queue) Dequeue() Element {
	ret := q.First()
	*q = (*q)[1:]
	return ret
}

func (q Queue) First() Element {
	if q.IsEmpty() {
		panic("Trying to get first element from an empty queue...")
	}
	return q[0]
}

func (q Queue) IsEmpty() bool {
	return len(q) == 0
}
