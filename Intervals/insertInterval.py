from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        starts = [x[0] for x in intervals]

        pos = bisect_left(starts, newInterval[0])

        intervals.insert(pos, newInterval)

        # Merge overlapping intervals
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # No overlap
                merged.append(interval)
            else:  # Overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged










