#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
from inspect import stack


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        s = list(s)
        par_mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        open_par = set(par_mapping.values())

        stack = []
        for i, char in enumerate(s):
            if char in open_par:
                stack.append(i)
            elif char in par_mapping:
                if stack:
                    expected = par_mapping[char]
                    if s[stack[-1]] == expected:
                        stack.pop()
                    else:
                        s[i] = ''
                else:
                    s[i] = ''

        while stack:
            s[stack[-1]] = ''
            stack.pop()

        return ''.join(s)


# @lc code=end
