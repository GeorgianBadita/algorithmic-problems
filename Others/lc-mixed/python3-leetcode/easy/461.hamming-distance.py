#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        for bit in range(31, -1, -1):
            x_bit = 1 if x & (1 << bit) else 0
            y_bit = 1 if y & (1 << bit) else 0
            if x_bit != y_bit:
                cnt += 1
        return cnt

# @lc code=end
