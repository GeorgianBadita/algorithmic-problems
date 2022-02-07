#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def gen_subsets(self, nums, sols, sol):
        for c_idx in range(0 if not sol else sol[-1] + 1, len(nums)):
            sol.append(c_idx)
            sols.append([nums[x] for x in sol])
            self.gen_subsets(nums, sols, sol)
            sol.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = [[]]
        self.gen_subsets(nums, sols, [])
        return sols
# @lc code=end
