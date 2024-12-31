

from typing import List


class Solution:

    def meet_room(self, intervals: List[List[int]]) -> bool:

        intervals = sorted(intervals, key=lambda x:x[0])

        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True



obj = Solution()


test = [[1, 3], [3, 5], [4, 6]]

print(obj.meet_room(test))


