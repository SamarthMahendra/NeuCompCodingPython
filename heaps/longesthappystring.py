class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []

        def helper(heap, payload, result):
            count, char = payload
            result.append(char)
            count += 1
            if count < 0:
                heapq.heappush(heap, (count, char))
            return

        while heap:
            count1, char1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break
                helper(heap, heapq.heappop(heap), result)

                heapq.heappush(heap, (count1, char1))
            else:
                helper(heap, (count1, char1), result)

        return "".join(result)
