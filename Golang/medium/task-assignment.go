package main

import "sort"

type SortWithIdx struct {
	sort.IntSlice
	idx []int
}

func (s SortWithIdx) Swap(i, j int) {
	s.IntSlice.Swap(i, j)
	s.idx[i], s.idx[j] = s.idx[j], s.idx[i]
}

func TaskAssignment(k int, tasks []int) [][]int {
	indices := []int{}
	for idx := 0; idx < 2*k; idx++ {
		indices = append(indices, idx)
	}

	sliceWithSort := SortWithIdx{IntSlice: tasks, idx: indices}
	sort.Sort(sliceWithSort)

	res := [][]int{}
	for idx := 0; idx < k; idx++ {
		res = append(res, []int{sliceWithSort.idx[idx], sliceWithSort.idx[2*k-idx-1]})
	}
	return res
}
