#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:

    def compute_perms(self, nums, used, perms, perm):
        for idx in range(len(nums)):
            if not used[idx]:
                used[idx] = True
                perm.append(nums[idx])
                if len(perm) == len(nums):
                    perms.append(perm[:])
                self.compute_perms(nums, used, perms, perm)
                perm.pop()
                used[idx] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.compute_perms(nums, [False]*len(nums), perms, [])
        return perms

# @lc code=end
