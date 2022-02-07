#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from operator import ne


class WordDictionary:

    def __init__(self):
        self.__trie = {}
        self.__stop = "$"

    def addWord(self, word: str) -> None:
        trie = self.__trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[self.__stop] = True

    def search(self, word):
        trie = self.__trie
        return self.__search(word, trie)

    def __search(self, word: str, trie) -> bool:
        for idx in range(len(word)):
            char = word[idx]
            if char == ".":
                exists = False
                for next in trie:
                    if next == self.__stop:
                        continue
                    exists = exists or self.__search(
                        word[idx + 1:], trie[next])
                return exists
            if char not in trie:
                return False
            trie = trie[char]
        return self.__stop in trie


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
