def findClosestValueInBst(root, target):
    closest_number = None

    queue = [root]

    while queue:
        current_node = queue.pop(0)

        if closest_number is None:
            closest_number = current_node.value

        elif abs(current_node.value - target) < abs(closest_number - target):
            closest_number = current_node.value

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return closest_number

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
