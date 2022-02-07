#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [(root, None)]
        sum_leaves = 0

        while queue:
            node, parent = queue.pop(0)
            if parent:
                if parent.left == node:
                    if not node.left and not node.right:
                        sum_leaves += node.val

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        return sum_leaves

# @lc code=end
