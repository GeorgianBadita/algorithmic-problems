#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = {x: chr(ord('A') + x) for x in range(26)}
        result = ""
        while columnNumber:
            if columnNumber == 26:
                result = "Z" + result
                break
            result = mapping[((columnNumber % 26 - 1) + 26) % 26] + result
            if columnNumber % 26 == 0:
                columnNumber = (columnNumber - 1) // 26
            else:
                columnNumber //= 26
        return result
# @lc code=end
