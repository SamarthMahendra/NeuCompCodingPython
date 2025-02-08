from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        print(dp)
        for t in range(amount+1):
            for c in coins:
                if t-c >= 0 :
                    dp[t] = min(dp[t], dp[t-c]+1)

        return dp[amount] if dp[amount]!= float('inf') else -1