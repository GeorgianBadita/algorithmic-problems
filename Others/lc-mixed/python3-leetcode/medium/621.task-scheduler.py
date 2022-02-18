#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        heap = []
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        for _, value in freq.items():
            heapq.heappush(heap, -value)

        curr_time = 0
        cooldown = {}

        while len(heap) > 0 or len(cooldown) > 0:
            if curr_time - n - 1 in cooldown:
                heapq.heappush(heap, -cooldown[curr_time - n - 1])
                del cooldown[curr_time - n - 1]

            if len(heap) > 0:
                left = -heap[0] - 1
                heapq.heappop(heap)
                if left != 0:
                    cooldown[curr_time] = left

            curr_time += 1

        return curr_time

# @lc code=end
