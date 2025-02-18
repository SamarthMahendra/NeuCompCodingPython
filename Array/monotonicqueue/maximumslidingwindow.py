class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dp = deque([])
        res = []
        for i, num in enumerate(nums):
            print(dp)
            if dp and dp[0][0] < i - k + 1:
                dp.popleft()

            while dp and dp[-1][1] < num:
                dp.pop()

            dp.append((i, num))

            if i >= k - 1:
                res.append(dp[0][1])

        return res




