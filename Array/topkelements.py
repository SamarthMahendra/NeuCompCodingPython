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
            if j < x :
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

    def topKFrequentv5(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        counts = Counter(nums)
        print(counts)
        heap_bucket = heapq.nlargest(k, counts.items(), key=lambda x: x[1])
        return [k for k, v in heap_bucket]

    def topKFrequentv6(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]

        for n, c in counts.items():
            freq[c].append(n)
        # bucket sort
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res


obj = Solution()
print(obj.topKFrequent([3,0,1,0],1))
