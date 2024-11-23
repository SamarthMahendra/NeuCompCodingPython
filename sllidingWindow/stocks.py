from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p

            else:
                current_profit = p - min_price
                max_profit = max(max_profit, current_profit)

        return max_profit


