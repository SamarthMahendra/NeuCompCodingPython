from collections import Counter
from collections import OrderedDict
from typing import List
# import heapq
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], x: int) -> List[int]:
        res = Counter(nums)
        res = OrderedDict(sorted(res.items(), key=lambda x: x[1],reverse=True))
        print(res)
        r = []
        j = 0
        for k, v in res.items():
            if j< x :
                r.append(k)
                j=j+1
            else:
                break
        return r

    def topKFrequentv2(self, nums: List[int], x: int) -> List[int]:
        fc = {}
        for n in nums:
            fc[n] = fc.get(n, 0) + 1

        li = []
        for k, v in fc.items():
            heapq.heappush(li, (-v, k))
        return [heapq.heappop(li)[1] for _ in range(x)]

    def topKFrequentv3(self, nums: List[int], k: int) -> List[int]:
        frequency_count = {}

        # Count the frequency of each number
        for num in nums:
            frequency_count[num] = frequency_count.get(num, 0) + 1

        # Sort the numbers based on their frequencies in descending order
        sorted_nums = sorted(frequency_count.keys(), key=lambda x: frequency_count[x], reverse=True)

        return sorted_nums[:k]

    def topKFrequentv4(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in Counter(nums).most_common(k)]

obj = Solution()
# test [3,0,1,0]
# k =
# 1
# Output
# [0]

print(obj.topKFrequent([3,0,1,0],1))
