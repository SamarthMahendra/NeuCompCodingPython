from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] =  prefix
            prefix = nums[i]* prefix
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]

        return res

    def productExceptSelfv2git (self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        product_without_zero = 1

        for i in nums:
            if i == 0:
                zeros += 1
            if zeros > 1:
                return [0] * len(nums)

            product = product * i
            product_without_zero = product_without_zero * i if i != 0 else product_without_zero
        return [product // i if i != 0 else product_without_zero for i in nums]