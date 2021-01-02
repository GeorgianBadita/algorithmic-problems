# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    stack = []
    last = None
    while stack or tree:
        while tree:
            stack.append(tree)
            tree = tree.left

        tree = stack.pop()
        if last == node:
            return tree
        last = tree
        tree = tree.right

    return None
