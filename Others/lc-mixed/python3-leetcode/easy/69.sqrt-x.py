#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

# @lc code=end
