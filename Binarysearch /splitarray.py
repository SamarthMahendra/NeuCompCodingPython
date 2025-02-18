class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_not_split(maxsum, k):
            cuts, cursum = 0, 0
            for x in nums:
                cursum = cursum + x
                if cursum > maxsum:
                    cuts += 1
                    cursum = x
            subs = cuts + 1
            return subs > k

        low, high = max(nums), sum(nums)
        while low < high:
            guess = (low + high) // 2
            if can_not_split(guess, k):
                low = guess + 1
            else:
                high = guess
        return low

