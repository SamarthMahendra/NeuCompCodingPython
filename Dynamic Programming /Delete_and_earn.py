from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_number = max(nums)
        dp = [0] * (max_number + 1)
        points = [0] * (max_number + 1)
        for i in nums:
            points[i] += i
        dp[1] = points[1]
        for i in range(2, max_number + 1):
            dp[i] = max(
                points[i] + dp[i - 2], dp[i - 1]
            )
        return dp[-1]
