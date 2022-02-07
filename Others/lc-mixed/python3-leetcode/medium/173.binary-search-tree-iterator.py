#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = []
        self.__push(root)

    def next(self) -> int:
        to_ret = self.__stack.pop()
        self.__push(to_ret.right)
        return to_ret.val

    def hasNext(self) -> bool:
        return self.__stack

    def __push(self, root):
        while root:
            self.__stack.append(root)
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
