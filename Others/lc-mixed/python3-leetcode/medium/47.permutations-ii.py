#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
import copy


class Solution:
    def bkt_per(self, nums, sols, sol, used):
        for idx in range(len(nums)):
            if not used[idx]:
                used[idx] = True
                sol.append(idx)
                if len(sol) == len(nums):
                    curr_sol = [nums[x] for x in copy.deepcopy(sol)]
                    sols.add(tuple(curr_sol))
                self.bkt_per(nums, sols, sol, used)
                used[idx] = False
                sol.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sols = set()
        self.bkt_per(nums, sols, [], [False] * len(nums))
        return [list(x) for x in sols]
# @lc code=end
