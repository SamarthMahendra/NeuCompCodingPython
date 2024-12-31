from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by ascending order
        intervals = sorted(intervals, key=lambda x: x[0])

        merged = []

        for start, end in intervals:

            if not merged or merged[-1][1] < start:
                merged.append([start, end])

            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged


