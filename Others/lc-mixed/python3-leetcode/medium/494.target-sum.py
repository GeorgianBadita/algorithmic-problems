#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def __init__(self):
        self.__map_candidate = {
            '-': lambda element: -1*element,
            '+': lambda element: element
        }

    def construct(self, curr_sum, nums, memo, target):
        key = (curr_sum, tuple(nums))
        if key in memo:
            return memo[key]
        if not nums:
            return 1 if curr_sum == target else 0
        result = self.construct(curr_sum - nums[0], nums[1:], memo, target) + self.construct(
            curr_sum + nums[0], nums[1:], memo, target)
        memo[key] = result
        return result

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.construct(0, nums, {}, target)
# @lc code=end
