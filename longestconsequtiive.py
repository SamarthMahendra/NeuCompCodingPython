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

obj = Solution()
print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) #

