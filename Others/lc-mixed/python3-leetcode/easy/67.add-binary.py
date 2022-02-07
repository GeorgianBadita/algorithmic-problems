#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        idx, jdx = len(a) - 1, len(b) - 1
        while idx >= 0 or jdx >= 0:
            a_value = a[idx] if idx >= 0 else "0"
            b_value = b[jdx] if jdx >= 0 else "0"
            res = ord(a_value) - ord('0') + ord(b_value) - ord('0') + carry
            carry = res // 2
            result += str(res % 2)
            idx, jdx = idx - 1, jdx - 1
        if carry:
            result += "1"

        return "".join(reversed(result))

# @lc code=end
