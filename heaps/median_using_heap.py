import heapq
class MedianFinder:
    def __init__(self):
        self.heaps = [], []



    def addNum(self, num):
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))


    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # We subtract `small[0]` from `large[0]`, because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian()) #1.5
obj.addNum(3)
print(obj.findMedian()) #2.0
obj.addNum(4)
print(obj.findMedian()) #2.5