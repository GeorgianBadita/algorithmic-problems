#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameter(self, root):
        if not root:
            return 0, 0
        left_diameter, left_depth = self.diameter(root.left)
        right_diameter, right_depth = self.diameter(root.right)
        return max(left_diameter, right_diameter, left_depth + right_depth), 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameter(root)[0]
        # @lc code=end
