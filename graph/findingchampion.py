# https://leetcode.com/problems/find-champion-ii/
from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n

        for u, v in edges:
            indegree[v] += 1

        res = [i for i, k in enumerate(indegree) if k == 0]
        return -1 if len(res) > 1 else res[0]

