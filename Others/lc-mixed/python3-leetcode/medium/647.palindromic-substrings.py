#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:

    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        res, i, n = 0, 0, len(s)

        while i < n:
            j, k = i - 1, i
            while k < n - 1 and s[k] == s[k + 1]:
                k += 1
            res += (k - j) * (k - j + 1) // 2
            i, k = k + 1, k + 1
            while j >= 0 and k < n and s[k] == s[j]:
                j -= 1
                k += 1
                res += 1
        return res

# @lc code=end
