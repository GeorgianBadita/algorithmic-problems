def iterativeInOrderTraversal(tree, callback):
    stack = []

    while tree or stack:
        while tree:
            stack.append(tree)
            tree = tree.left

        tree = stack.pop()
        callback(tree)
        tree = tree.right
