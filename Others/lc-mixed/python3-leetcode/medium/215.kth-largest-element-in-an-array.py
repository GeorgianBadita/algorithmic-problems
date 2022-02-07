#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for elem in nums:
            heapq.heappush(heap, elem)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
# @lc code=end
