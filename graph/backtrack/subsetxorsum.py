class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(i, cursum):
            nonlocal total
            if i == len(nums):
                total += cursum

                return

            backtrack(i + 1, cursum)
            backtrack(i + 1, cursum ^ nums[i])
            return

        backtrack(0, 0)
        return total
