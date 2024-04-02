
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 1
        while i < l and i > 0:
            if nums[i-1] == nums[i]:
                nums = nums[:i-1] + nums[i:]
                i = i-1
        return nums


obj = Solution()
# [1, 1, 2]
print(obj.removeDuplicates([1,1,2])) # 2