# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_depth(tree):
    if not tree:
        return 0

    return 1 + max(get_depth(tree.left), get_depth(tree.right))


def binaryTreeDiameter(tree):
    if not tree:
        return 0

    left_depth = get_depth(tree.left)
    right_depth = get_depth(tree.right)

    return max(left_depth + right_depth, binaryTreeDiameter(tree.left), binaryTreeDiameter(tree.right))
