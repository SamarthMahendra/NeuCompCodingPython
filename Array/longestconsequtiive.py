from collections import defaultdict
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        m = 0
        count = 0
        for i in range(len(sorted_nums)):
            if i == 0:
                count = 1
            else:
                if sorted_nums[i] == sorted_nums[i-1] + 1:
                    count = count + 1
                elif sorted_nums[i] == sorted_nums[i-1]:
                    continue
                else:
                    count = 1
            m = max(count, m)
        return m


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Eliminate duplicates and allow O(1) lookups
        longest = 0

        for num in num_set:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                while (num := num + 1) in num_set:  # Use walrus operator for concise updating
                    length += 1
                longest = max(longest, length)

        return longest


obj = Solution()
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #

