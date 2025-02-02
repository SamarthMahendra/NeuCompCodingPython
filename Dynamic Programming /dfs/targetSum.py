class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}  # key: (index, current_sum)

        def dfs(index: int, current_sum: int) -> int:
            # Base case: when we've processed all numbers, check if we've hit the target
            if index == len(nums):
                return 1 if current_sum == target else 0

            # If this state has been computed before, return the cached value.
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            # Choose the '+' sign for nums[index]
            add = dfs(index + 1, current_sum + nums[index])
            # Choose the '-' sign for nums[index]
            subtract = dfs(index + 1, current_sum - nums[index])

            # Cache and return the total ways from this state.
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]

        return dfs(0, 0)

