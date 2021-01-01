# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sum(root, curr_sum):

    if not root.left and not root.right:
        return [curr_sum + root.value]

    if root.left and root.right:
        return branch_sum(root.left, curr_sum + root.value) + branch_sum(root.right, curr_sum + root.value)
    elif root.left:
        return branch_sum(root.left, curr_sum + root.value)
    elif root.right:
        return branch_sum(root.right, curr_sum + root.value)


def branchSums(root):
    return branch_sum(root, 0)
