from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)

        presum = [0] * (n + 1)
        for i in range(n):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                l = 1
            else:
                l = 0
            presum[i + 1] = presum[i] + l

        res = []
        for q in queries:

            count = presum[q[1]+1] - presum[q[0]]
            res.append(count)

        return res


