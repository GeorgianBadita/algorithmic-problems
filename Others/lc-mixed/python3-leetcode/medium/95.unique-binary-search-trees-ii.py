#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy


class Solution:
    def insert_in_bst(self, root, val):
        new_node = TreeNode(val)
        parent = None
        while root:
            parent = root
            if val > root.val:
                root = root.right
            else:
                root = root.left
        if not parent:
            parent = new_node
        elif val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
        return parent

    def generate(self, start, end):
        if start > end:
            return [None]

        all_trees = []
        for root_val in range(start, end + 1):
            all_left = self.generate(start, root_val - 1)
            all_right = self.generate(root_val + 1, end)

            for left_tree in all_left:
                for right_tree in all_right:
                    root = TreeNode(root_val)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)
        return all_trees

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n)
# @lc code=end
