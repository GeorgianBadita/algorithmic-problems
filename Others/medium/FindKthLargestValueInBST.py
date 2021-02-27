# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    stack = []

    while stack or tree:
        while tree:
            stack.append(tree)
            tree = tree.right

        tree = stack.pop()
        k -= 1
        if k == 0:
            return tree.value
        tree = tree.left
