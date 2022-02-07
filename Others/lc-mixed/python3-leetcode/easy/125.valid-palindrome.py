#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        string = []
        for char in s:
            if ord('A') <= ord(char) <= ord('Z'):
                char = chr(ord('a') + (ord(char) - ord('A')))
            if not (ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')):
                continue
            string.append(char)
        return ''.join(string) == ''.join(string[::-1])
# @lc code=end
