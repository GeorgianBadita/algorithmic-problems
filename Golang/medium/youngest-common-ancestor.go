package main

type AncestralTree struct {
	Name     string
	Ancestor *AncestralTree
}

func GetYoungestCommonAncestor(top, descendantOne, descendantTwo *AncestralTree) *AncestralTree {
	path := map[AncestralTree]bool{}

	for descendantOne != nil {
		path[*descendantOne] = true
		descendantOne = descendantOne.Ancestor
	}

	for descendantTwo != nil {
		_, ok := path[*descendantTwo]
		if ok {
			return descendantTwo
		}
		descendantTwo = descendantTwo.Ancestor
	}
	return nil
}
