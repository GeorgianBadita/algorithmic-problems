#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        while last >= 0 and s[last] == ' ':
            last -= 1
        length = 0
        while last >= 0 and s[last] != ' ':
            length += 1
            last -= 1
        return length
# @lc code=end
