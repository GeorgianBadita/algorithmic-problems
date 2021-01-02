def minHeightBst(array):
    return construct_bst_aux(array, 0, len(array) - 1)


def construct_bst_aux(array, left, right):
    if left == right:
        return BST(array[left])

    if left + 1 == right:
        root = BST(array[left])
        root.right = BST(array[right])
        return root

    mid = (left + right) // 2

    root = BST(array[mid])

    root.left = construct_bst_aux(array, left, mid - 1)
    root.right = construct_bst_aux(array, mid + 1, right)

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
