#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def validate_bst(self, root, min, max):
        if not root:
            return True
        is_current_bst = min < root.val < max
        return self.validate_bst(root.left, min, root.val) and is_current_bst and self.validate_bst(root.right, root.val, max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate_bst(root, float('-inf'), float('inf'))
        # @lc code=end
