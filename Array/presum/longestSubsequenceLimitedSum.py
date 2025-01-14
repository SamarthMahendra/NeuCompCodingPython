from typing import List
from itertools import accumulate
from bisect import bisect_left

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presum = [0] + list(accumulate(nums))
        res = []
        for q in queries:
            i = bisect_left(presum, q+1)
            r = i-1 if i-1 >= 0 else 0
            res.append(r)
        return res
