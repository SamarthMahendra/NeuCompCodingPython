
# just loop through twice
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * len(nums)
        nums = nums + nums
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                res[index % n] = nums[i]
            stack.append(i)
        return res


