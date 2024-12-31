from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        prev_interval, count = intervals[0], 1

        for start, end in intervals[1:]:

            if start >= prev_interval[1]:
                count += 1
                prev_interval = i

        return len(intervals) - count


