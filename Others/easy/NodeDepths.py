def node_depths(root, curr_depth):
    if not root:
        return 0

    return curr_depth + node_depths(root.left, curr_depth + 1) + node_depths(root.right, curr_depth + 1)


def nodeDepths(root):
    return node_depths(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
