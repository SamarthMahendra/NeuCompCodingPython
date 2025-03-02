class Solution:

    def numSquares(self, n: int) -> int:
        import math

        sqaures = [i * i for i in range(1, int(math.sqrt(n)) + 1)]

        @cache
        def dp(rem):
            if rem == 0:
                return 0

            min_count = float('inf')
            for sq in sqaures:
                if rem < sq:
                    break
                min_count = min(min_count, 1 + dp(rem - sq))
            return min_count

        return dp(n)


