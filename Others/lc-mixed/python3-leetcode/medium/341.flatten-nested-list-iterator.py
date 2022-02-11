#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.__nested_integer = self.__unpack(nestedList)
        self.__idx = 0

    def next(self) -> int:
        to_ret = self.__nested_integer[self.__idx]
        self.__idx += 1
        return to_ret

    def hasNext(self) -> bool:
        return self.__idx < len(self.__nested_integer)

    def __unpack(self, nested_list):
        if not nested_list:
            return []
        if nested_list[0].isInteger():
            return [nested_list[0].getInteger()] + self.__unpack(nested_list[1:])
        return self.__unpack(nested_list[0].getList()) + self.__unpack(nested_list[1:])


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
