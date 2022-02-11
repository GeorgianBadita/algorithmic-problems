#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        queue = [root]
        parent = {}

        while queue:
            node = queue.pop(0)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        p_path = set([p])
        while p in parent:
            p = parent[p]
            p_path.add(p)

        while q in parent:
            if q in p_path:
                return q
            q = parent[q]
        if q in p_path:
            return q
# @lc code=end
