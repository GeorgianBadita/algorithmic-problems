#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.__stop = "$"
        self.__trie = {}

    def insert(self, word: str) -> None:
        trie = self.__trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[self.__stop] = True

    def search(self, word: str) -> bool:
        trie = self.__trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        return self.__stop in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.__trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
