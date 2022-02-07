#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [(root, None)]
        while queue:
            node, parent = queue.pop(0)
            if parent:
                if node == parent.left:
                    if parent.right:
                        node.next = parent.right
                    else:
                        if parent.next:
                            if parent.next.left:
                                node.next = parent.next.left
                            else:
                                node.next = parent.next.right
                elif node == parent.right:
                    if parent.next:
                        if parent.next.left:
                            node.next = parent.next.left
                        else:
                            node.next = parent.next.right

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        return root
# @lc code=end
