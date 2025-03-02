from typing import List


# so max area is one of where atleast one bar is full included,
# we just have to find next smaller and prev smaller so that we can get width till where we can extend


class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        def next_smaller(nums):
            stack = []
            res = [-1] * len(nums)

            for i in range(len(nums)):

                while stack and nums[stack[-1]] > nums[i]:
                    index = stack.pop()
                    res[index] = i

                stack.append(i)
            return res

        def prev_smaller(nums):
            stack = []
            res = [-1] * len(nums)

            for i in range(len(nums)):

                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if stack:
                    res[i] = stack[-1]
                stack.append(i)

            return res

        p = prev_smaller(nums)
        n = next_smaller(nums)

        max_area = float('-inf')

        for i in range(len(nums)):
            width = (n[i] if n[i] != -1 else len(nums)) - (p[i]) - 1
            max_area = max(max_area, width * nums[i])
        return max_area

    class Solution:
        def largestRectangleArea(self, nums: List[int]) -> int:

            stack = []
            nums.append(0)
            max_area = 0
            for i in range(len(nums)):

                while stack and nums[stack[-1]] > nums[i]:
                    index = stack.pop()
                    height = nums[index]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, w * height)
                stack.append(i)
            return max_area



