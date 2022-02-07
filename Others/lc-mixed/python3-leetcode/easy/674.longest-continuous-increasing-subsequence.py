#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr_size, best_size = 1, 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_size += 1
            else:
                best_size = max(curr_size, best_size)
                curr_size = 1
        return max(curr_size, best_size)
# @lc code=end
