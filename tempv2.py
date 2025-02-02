
from typing import List
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        bucket = sorted(nums[:k])

        def get_median(nums):
            if len(nums) % 2 == 0:
                p = len(nums) // 2
                median = (nums[p] + nums[p - 1]) // 2
            else:
                p = len(nums) // 2
                median = nums[p]

            return median

        res = []

        for i in range(k, len(nums)):
            res.append(get_median(bucket))

            bisect.insort(bucket, nums[i])

            bucket.remove(nums[i - k])
        res.append(get_median(bucket))
        return res




nums = [1,3,-1,-3,5,3,6,7]
k = 3


obj = Solution()
print(obj.medianSlidingWindow(nums, k))











