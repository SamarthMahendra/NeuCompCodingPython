class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        presum_count = defaultdict(int)
        presum = 0
        count = 0

        presum_count[0] = 1

        for i in nums:
            presum += i

            if presum - k in presum_count:
                count += presum_count[presum - k]

            presum_count[presum] += 1

        return count



