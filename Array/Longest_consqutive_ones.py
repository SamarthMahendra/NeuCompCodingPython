# from typing import List
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0
#         for right in range(len(nums)):
#             # If we included a zero in the window we reduce the value of k.
#             # Since k is the maximum zeros allowed in a window.
#             k -= 1 - nums[right]
#             # A negative k denotes we have consumed all allowed flips and window has
#             # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
#             if k < 0:
#                 # If the left element to be thrown out is zero we increase k.
#                 k += 1 - nums[left]
#                 left += 1
#         print(right)
#         print(left)
#         return right - left + 1

from typing import List
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    from itertools import groupby
    for i, k in groupby(nums):
        print(i, list(k))


findMaxConsecutiveOnes([1,1,1,1,0,1,1,0,0,1])