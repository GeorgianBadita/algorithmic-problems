#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class Node:
    def __init__(self, next=None, prev=None, val=None):
        self.next = next
        self.prev = prev
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__start = None
        self.__end = None
        self.__cache = {}

    def get(self, key: int) -> int:
        value = self.__cache.get(key, Node(val=(-1, -1)))
        if key in self.__cache:
            self.__delete_node(self.__cache[key])
            self.__cache[key] = self.__add_to_end(value.val)
        return value.val[1]

    def put(self, key: int, value: int) -> None:
        if len(self.__cache) == self.__capacity and key not in self.__cache:
            del self.__cache[self.__start.val[0]]
            self.__delete_node(self.__start)
        if not key in self.__cache:
            self.__cache[key] = self.__add_to_end((key, value))
        else:
            self.__delete_node(self.__cache[key])
            del self.__cache[key]
            self.__cache[key] = self.__add_to_end((key, value))

    def __delete_node(self, node):
        if not node:
            return
        if self.__start == self.__end == node:
            self.__start = None
            self.__end = None
        elif node == self.__start:
            self.__start = self.__start.next
            self.__start.prev = None
        elif node == self.__end:
            self.__end = self.__end.prev
            self.__end.next = None
        else:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        del node

    def __add_to_end(self, tup):
        if self.__end is None:
            self.__start = Node(val=tup)
            self.__end = self.__start
            self.__end.prev = self.__start
            self.__start.next = self.__end
            self.__end.next = None
            self.__start.prev = None
            return self.__start
        else:
            new_node = Node(val=tup)
            new_node.prev = self.__end
            self.__end.next = new_node
            self.__end = new_node
            return new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
