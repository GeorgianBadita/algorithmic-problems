#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def can_target(self, root, target, seen):
        if not root:
            return False

        can_do = False
        if target - root.val in seen:
            can_do = True
        seen.add(root.val)
        return self.can_target(root.left, target, seen) or self.can_target(root.right, target, seen) or can_do

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.can_target(root, k, set())
# @lc code=end
