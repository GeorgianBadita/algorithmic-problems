#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def are_tree_same(self, root1, root2):
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1) or root1.val != root2.val:
            return False
        return self.are_tree_same(root1.left, root2.left) and self.are_tree_same(root1.right, root2.right)

    def isSubtree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        queue = [root1]
        exists_subroot = False
        while queue:
            node = queue.pop(0)
            if node.val == root2.val:
                exists_subroot = exists_subroot or self.are_tree_same(
                    node, root2)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return exists_subroot
        # @lc code=end
