# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # end early and non overlapping
        intervals.sort(key=lambda x:x[1], reverse=False)

        preve = intervals[0][1]
        count = 1

        for s, e in intervals[1:]:
            if s >= preve:
                preve = e
                count += 1
        return len(intervals) - count
