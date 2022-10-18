from typing import List


class Solution:
    def can_merge(self, in1, in2):
        return in2[0] <= in1[1]

    def merge(self, in1, in2):
        return [min(in1[0], in2[0]), max(in1[1], in2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_pos = 0
        while insert_pos < len(intervals) and (
                intervals[insert_pos][0] < newInterval[0] or intervals[insert_pos][0] == newInterval[0] and newInterval[
            1] <= intervals[insert_pos][0]):
            insert_pos += 1

        insert_pos_back = insert_pos - 1
        curr_int = newInterval
        while insert_pos_back >= 0 and self.can_merge(intervals[insert_pos_back], curr_int):
            curr_int = self.merge(intervals[insert_pos_back], curr_int)
            insert_pos_back -= 1

        insert_pos_front = insert_pos
        while insert_pos_front < len(intervals) and self.can_merge(curr_int, intervals[insert_pos_front]):
            curr_int = self.merge(intervals[insert_pos_front], curr_int)
            insert_pos_front += 1

        return intervals[:insert_pos_back + 1] + [curr_int] + intervals[insert_pos_front:]


print(Solution().insert([[1,3],[6,9]], [2, 5]))
