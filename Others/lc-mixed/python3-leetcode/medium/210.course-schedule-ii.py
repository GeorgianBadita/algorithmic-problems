#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deg = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for y, x in prerequisites:
            deg[y] += 1
            graph[x].append(y)

        queue = [x for x in range(len(deg)) if deg[x] == 0]
        topo_sort = []

        while queue:
            node = queue.pop()
            topo_sort.append(node)

            for adj in graph[node]:
                deg[adj] -= 1
                if deg[adj] == 0:
                    queue.append(adj)
        return topo_sort if len(topo_sort) == numCourses else []

# @lc code=end
