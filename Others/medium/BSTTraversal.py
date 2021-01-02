def inOrderTraverse(tree, array):
    stack = []

    while stack or tree:
        while tree:
            stack.append(tree)
            tree = tree.left

        tree = stack.pop()
        array.append(tree.value)
        tree = tree.right
    return array


def preOrderTraverse(tree, array):
    stack = [tree]
    while stack:
        curr_node = stack.pop()
        array.append(curr_node.value)
        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.left)

    return array


def post_order(tree):
    if not tree:
        return []
    return post_order(tree.left) + post_order(tree.right) + [tree.value]


def postOrderTraverse(tree, array):
    array = post_order(tree)
    return array
