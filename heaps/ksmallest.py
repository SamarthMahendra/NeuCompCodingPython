import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        bucket = []
        for p in points:
            heapq.heappush(bucket, ((p[0] ** 2) + (p[1] ** 2), p))

        res = []
        for i in range(k):
            res.append(heapq.heappop(bucket)[1])
        return res


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: (x[0] ** 2) + (x[1] ** 2))





