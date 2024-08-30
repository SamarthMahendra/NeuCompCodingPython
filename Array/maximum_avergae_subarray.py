from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[0:k])
        cur = maxsum
        for i in range(k, len(nums)):
            cur = cur + nums[i] - nums[i - k]
            maxsum = max(maxsum, cur)
        return maxsum / k
