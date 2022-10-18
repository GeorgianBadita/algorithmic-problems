from typing import List


class Solution:

    def can_merge(self, interval1, interval2):
        return interval2[0] <= interval1[1]

    def merge_ints(self, interval1, interval2):
        return [interval1[0], max(interval2[1], interval1[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []

        curr_interval = intervals[0]
        for idx in range(1, len(intervals)):
            if self.can_merge(curr_interval, intervals[idx]):
                curr_interval = self.merge_ints(curr_interval, intervals[idx])
            else:
                result.append(curr_interval)
                curr_interval = intervals[idx]

        if not result or curr_interval != result[-1]:
            result.append(curr_interval)

        return result

print(Solution().merge([[1,4],[4,5]]))