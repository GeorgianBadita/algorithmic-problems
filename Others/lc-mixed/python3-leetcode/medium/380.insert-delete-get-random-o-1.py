#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:

    def __init__(self):
        self.__map = {}
        self.__values = []

    def insert(self, val: int) -> bool:
        if val in self.__map:
            return False

        self.__map[val] = len(self.__values)
        self.__values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.__map:
            return False

        last_element = self.__values[-1]
        to_remove_index = self.__map[val]

        self.__map[last_element] = to_remove_index
        self.__values[to_remove_index] = last_element

        self.__values.pop()
        del self.__map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.__values)
        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
        # @lc code=end
