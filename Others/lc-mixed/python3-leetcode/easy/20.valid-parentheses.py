#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0
# @lc code=end
