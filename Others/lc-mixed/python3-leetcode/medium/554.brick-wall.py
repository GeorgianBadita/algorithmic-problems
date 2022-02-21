#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return 0

        edges, max_edges = {}, 0
        max_s = sum(wall[0])
        for row in wall:
            idx, curr_sum = 0, row[0]
            while idx < len(row) and curr_sum < max_s:
                edges[curr_sum] = edges.get(curr_sum, 0) + 1
                max_edges = max(max_edges, edges[curr_sum])
                idx += 1
                curr_sum += row[idx]
        return len(wall) - max_edges

# @lc code=end
