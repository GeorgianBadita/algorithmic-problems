# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height_balanced_helper(tree):
    if not tree:
        return True, -1

    left_tree_balanced, left_height = height_balanced_helper(tree.left)
    right_tree_balanced, right_height = height_balanced_helper(tree.right)

    height = max(left_height, right_height) + 1
    return left_tree_balanced and right_tree_balanced and abs(left_height - right_height) <= 1, height


def heightBalancedBinaryTree(tree):
    balanced, _ = height_balanced_helper(tree)
    return balanced
