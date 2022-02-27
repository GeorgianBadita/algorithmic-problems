#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    # PAYPALISHIRING, numRows = 6
    # P   A   H   N
    # A P L S I I G
    # Y   I   R

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        index, step = 0, 1
        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(res)
# @lc code=end
