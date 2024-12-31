class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from bisect import bisect_left

        res = set()
        nums.sort()
        for i in range(len(nums)):
            idx = bisect_left(nums, nums[i] - k)
            if idx >= 0 and idx != i and abs(nums[idx] - nums[i]) == k:
                if (nums[idx], nums[i]) not in res:
                    res.add((nums[i], nums[idx]))
        return len(res)






