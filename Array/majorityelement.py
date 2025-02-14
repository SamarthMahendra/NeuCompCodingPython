class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)//2

        counter = Counter(nums)
        for key, count in counter.items():
            if count > n:
                return key
