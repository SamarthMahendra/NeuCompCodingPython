from typing import List
from functools import lru_cache




class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            max_length = 1  # The cell itself counts as length 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_length = max(max_length, 1 + dfs(nr, nc))
            return max_length

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c))

        return res
