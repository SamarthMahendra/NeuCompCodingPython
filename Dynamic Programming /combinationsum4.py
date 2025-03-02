class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(rem):
            if rem == 0:
                return 1
            if rem < 0:
                return 0

            total = 0
            for n in nums:
                total += dp(rem - n)
            return total

        return dp(target)
