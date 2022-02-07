#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def get_freq(self, word):
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord('a')] += 1
        return tuple(freq)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            anagram = self.get_freq(word)
            if anagram in groups:
                groups[anagram].append(word)
            else:
                groups[anagram] = [word]
        return list(groups.values())

# @lc code=end
