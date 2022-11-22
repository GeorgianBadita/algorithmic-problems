package main

// Do not edit the class below except for the
// PopulateSuffixTrieFrom and Contains methods.
// Feel free to add new properties and methods
// to the class.
type SuffixTrie map[byte]SuffixTrie

// Feel free to add to this function.
func NewSuffixTrie() SuffixTrie {
	trie := SuffixTrie{}
	return trie
}

func (trie SuffixTrie) PopulateSuffixTrieFrom(str string) {
	// Write your code here.
}

func (trie SuffixTrie) Contains(str string) bool {
	// Write your code here.
	return false
}
