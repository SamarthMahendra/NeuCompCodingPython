from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the count of prefix sums
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1  # Initialize for subarrays starting at the beginning
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num  # Update the running sum

            # Check if (current_sum - k) exists in prefix_sum_counts
            if current_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[current_sum - k]

            # Update the frequency of the current_sum
            prefix_sum_counts[current_sum] += 1

        return count
