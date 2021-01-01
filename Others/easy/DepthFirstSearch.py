# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]

        while stack:
            current_node = stack.pop()
            array.append(current_node.name)
            for i in range(len(current_node.children) - 1, -1, -1):
                stack.append(current_node.children[i])
        return array
