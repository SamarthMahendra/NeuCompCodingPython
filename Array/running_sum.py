from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(k for k in nums[:i + 1]) for i in range(len(nums))]
