from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp(target, count):
            if target == amount:
                return count
            if target > amount:
                return float('inf')
            min_c = float('inf')
            for i in coins:
                min_c = min(min_c, dp(target + i, count + 1))
            return min_c

        return dp(0, 0)



a = [1,2,5]

s = Solution()
print(s.coinChange(a, 11))  # Output: 3
