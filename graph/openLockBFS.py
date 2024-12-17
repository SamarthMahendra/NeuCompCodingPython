from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        deadends = set(deadends)
        if start in deadends:
            return -1

        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            cur, steps = queue.popleft()

            if cur == target:
                return steps

            for i in range(4):
                cur_digit = int(cur[i])

                forward = cur[:i] + str((cur_digit + 1) % 10) + cur[i + 1:]
                if forward not in visited and forward not in deadends:
                    queue.append((forward, steps + 1))
                    visited.add(forward)

                backward = cur[:i] + str((cur_digit - 1) % 10) + cur[i + 1:]
                if backward not in visited and backward not in deadends:
                    queue.append((backward, steps + 1))
                    visited.add(backward)

        return -1
