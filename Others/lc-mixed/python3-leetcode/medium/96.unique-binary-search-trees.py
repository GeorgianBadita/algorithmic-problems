#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
import math


class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2*n)//(math.factorial(n)*math.factorial(n + 1))
# @lc code=end
