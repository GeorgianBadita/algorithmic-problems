#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def gen_sols(self, nums, sols, sol):
        for c_idx in range(0 if not sol else sol[-1] + 1, len(nums)):
            sol.append(c_idx)
            sols.append([nums[x] for x in sol])
            self.gen_sols(nums, sols, sol)
            sol.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sols = [[]]
        self.gen_sols(sorted(nums), sols, [])
        return [list(x) for x in set([tuple(x) for x in sols])]
# @lc code=end
