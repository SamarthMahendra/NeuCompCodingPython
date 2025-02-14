class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        temp = Counter(nums)
        i = 0
        for n in [0, 1, 2]:
            for c in range(temp[n]):
                nums[i] = n
                i += 1


