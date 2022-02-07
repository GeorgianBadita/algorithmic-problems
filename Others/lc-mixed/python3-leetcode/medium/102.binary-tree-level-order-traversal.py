#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level_traversal = []
        queue = [(root, 0)]
        while queue:
            node, curr_level = queue[0]
            queue.pop(0)
            if curr_level == len(level_traversal):
                level_traversal.append([node.val])
            else:
                level_traversal[curr_level].append(node.val)

            if node.left:
                queue.append((node.left, curr_level + 1))
            if node.right:
                queue.append((node.right, curr_level + 1))

        return level_traversal
# @lc code=end
