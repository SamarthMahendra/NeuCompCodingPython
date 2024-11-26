class Solution:
    def climbStairs(self, n: int) -> int:

        def countWays(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            return countWays(n - 1) + countWays(n - 2)

        return countWays(n)

    def climbStairsv2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            # T(n) = T(n-1) + T(n-2)

        bucket = [0] * (n + 1)

        bucket[1] = 1
        bucket[2] = 2

        for i in range(3, n + 1):  # Iterate from 3 to n
            bucket[i] = bucket[i - 1] + bucket[i - 2]  # Fill each position based on the formula

        return bucket[n]

