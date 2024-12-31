from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_finish(piles, k):
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
            return hour <= h

        low, high = 1, max(piles)
        result = high

        while low <= high:
            mid = (low + high)//2
            if can_finish(piles, mid):
                res = mid
                high = high - 1
            else:
                low = low + 1
        return res

