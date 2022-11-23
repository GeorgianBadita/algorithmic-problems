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
	for idx := len(str) - 1; idx >= 0; idx-- {
		slice := str[idx:]

		addSliceToTrie(trie, slice)
	}
}

func (trie SuffixTrie) Contains(str string) bool {
	currTrie := trie
	for sliceIdx := 0; sliceIdx < len(str); sliceIdx++ {
		byte := str[sliceIdx]
		if nextTrie, ok := currTrie[byte]; ok {
			currTrie = nextTrie
		} else {
			return false
		}
	}

	_, ok := currTrie['*']
	return ok
}

func addSliceToTrie(trie SuffixTrie, slice string) {
	currTrie := trie
	for sliceIdx := 0; sliceIdx < len(slice); sliceIdx++ {
		byte := slice[sliceIdx]
		if nextTrie, ok := currTrie[byte]; ok {
			currTrie = nextTrie
		} else {
			currTrie[byte] = NewSuffixTrie()
			currTrie = currTrie[byte]
		}
	}
	currTrie['*'] = nil
}

func main() {
	trie := NewSuffixTrie()
	trie.PopulateSuffixTrieFrom("testtest")
}
