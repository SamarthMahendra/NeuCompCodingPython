from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        from collections import Counter

        ref_counter = Counter(p)
        s_counter = Counter()
        window = len(p)
        res = []

        for i, char in enumerate(s):

            s_counter[char] += 1

            if i >= window:

                if s_counter[s[i - window]] == 1:
                    del s_counter[s[i - window]]
                else:
                    s_counter[s[i - window]] -= 1

            if ref_counter == s_counter:
                res.append(i - window + 1)

        return res
