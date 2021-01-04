# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    d1 = get_depth(topAncestor, descendantOne)
    d2 = get_depth(topAncestor, descendantTwo)

    if d1 > d2:
        return backtrack(descendantOne, descendantTwo, d1 - d2)

    return backtrack(descendantTwo, descendantOne, d2 - d1)


def get_depth(top, curr):
    if curr == top:
        return 0
    return 1 + get_depth(top, curr.ancestor)


def backtrack(low, high, diff):
    while diff > 0:
        low = low.ancestor
        diff -= 1

    while low != high:
        low = low.ancestor
        high = high.ancestor

    return low
