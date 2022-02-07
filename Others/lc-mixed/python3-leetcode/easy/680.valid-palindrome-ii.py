#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def can_be_palindrome_ignore(self, s, pos):
        left, right = 0, len(s) - 1
        while left < right:
            if left == pos:
                left += 1
                continue
            if right == pos:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.can_be_palindrome_ignore(s, left) or self.can_be_palindrome_ignore(s, right)
            left += 1
            right -= 1

        return True
# @lc code=end
