#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct_paths(self, root, sols, current_path):
        if not root:
            return
        if not root.left and not root.right:
            sols.append(current_path + [root.val])
            return

        self.construct_paths(root.left, sols, current_path + [root.val])
        self.construct_paths(root.right, sols, current_path + [root.val])

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        sols = []
        self.construct_paths(root, sols, [])
        return ['->'.join([str(x) for x in path]) for path in sols]
# @lc code=end
