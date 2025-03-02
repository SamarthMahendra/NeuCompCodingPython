class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(remaining=k, cur=[], start=1):
            if remaining == 0:
                res.append(cur.copy())
                return

            for i in range(start, n + 1):
                newcur = cur + [i]
                backtrack(remaining - 1, newcur, i + 1)
            return

        backtrack()
        return res