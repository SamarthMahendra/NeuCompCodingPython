from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        ref = Counter(words)

        window_map = Counter()

        k = len(words[0])
        window_size = 0

        res = []
        l = 0
        for r in range(0, len(s), k):

            sub_string = s[r:r + k]
            window_map[sub_string] += 1
            window_size += 1

            if window_size > len(words):
                del_str = s[l:l + k]
                if window_map[del_str] == 1:
                    del window_map[del_str]
                    l += k
                    window_size -= 1
                else:
                    window_map[del_str] -= 1
                    l += k
                    window_size -= 1

            if window_map == ref:
                res.append(l)

        return res


s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

obj = Solution()
print(obj.findSubstring(s, words))



