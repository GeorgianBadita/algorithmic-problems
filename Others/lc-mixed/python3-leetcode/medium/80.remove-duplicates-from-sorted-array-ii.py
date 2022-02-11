#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_ptr = 1
        cnt_at_ptr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[unique_ptr - 1] and cnt_at_ptr == 1:
                nums[unique_ptr] = nums[i]
                unique_ptr += 1
                cnt_at_ptr = 0
            elif nums[i] != nums[unique_ptr - 1]:
                nums[unique_ptr] = nums[i]
                unique_ptr += 1
                cnt_at_ptr = 1
        return unique_ptr

# @lc code=end
