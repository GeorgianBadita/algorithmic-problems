# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]

        while queue:
            curr_node = queue.pop(0)
            array.append(curr_node.name)
            for node in curr_node.children:
                queue.append(node)

        return array
