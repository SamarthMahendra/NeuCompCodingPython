class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_char, prev_count = None, 0

        while heap:

            count, char = heapq.heappop(heap)

            result.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            prev_char, prev_count = char, count + 1
        return ''.join(result)

