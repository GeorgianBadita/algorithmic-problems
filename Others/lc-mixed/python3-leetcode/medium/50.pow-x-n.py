#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:

    def pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 1:
            return x * self.pow(x, n - 1)
        else:
            half_power = self.pow(x, n // 2)
            return half_power * half_power

    def myPow(self, x: float, n: int) -> float:
        return self.pow(1/x if n < 0 else x, -n if n < 0 else n)
# @lc code=end
