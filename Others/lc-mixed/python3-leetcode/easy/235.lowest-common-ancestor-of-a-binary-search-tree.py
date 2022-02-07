#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        parent[root] = None
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        p_path = set()
        node = p
        while node:
            p_path.add(node)
            node = parent[node]
        node = q
        while node:
            if node in p_path:
                return node
            node = parent[node]
        return None
# @lc code=end
