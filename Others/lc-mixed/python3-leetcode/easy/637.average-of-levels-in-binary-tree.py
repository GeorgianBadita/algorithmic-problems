#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sums = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if level == len(level_sums):
                level_sums.append([node.val, 1])
            else:
                curr_sum, num_els = level_sums[level]
                level_sums[level] = [curr_sum + node.val, num_els + 1]
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return [s / x for s, x in level_sums]
# @lc code=end
