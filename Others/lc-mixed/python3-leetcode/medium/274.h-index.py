#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:

    def is_valid_h_index(self, citations, value):
        greater_equal = 0
        for citation in citations:
            if citation >= value:
                greater_equal += 1
        return greater_equal >= value

    def h_index_bin(self, citations, max_citation):
        left, right = 0, max_citation

        while left <= right:
            mid_index = left + (right - left) // 2
            is_mid_valid_index = self.is_valid_h_index(citations, mid_index)
            if is_mid_valid_index and not self.is_valid_h_index(citations, mid_index + 1):
                return mid_index
            if is_mid_valid_index:
                left = mid_index + 1
            else:
                right = mid_index - 1
        return -1

    def hIndex(self, citations: List[int]) -> int:
        max_citation = max(citations)
        return self.h_index_bin(citations, max_citation)
# @lc code=end
