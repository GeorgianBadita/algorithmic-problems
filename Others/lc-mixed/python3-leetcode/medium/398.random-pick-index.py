#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.__nums = self.__process(nums)

    def pick(self, target: int) -> int:
        return random.choice(self.__nums[target])

    def __process(self, nums):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = [i]
            else:
                map[nums[i]].append(i)
        return map


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
