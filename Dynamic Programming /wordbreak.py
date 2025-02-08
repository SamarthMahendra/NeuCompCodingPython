from typing import List
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = max([len(i) for i in wordDict])

        @cache
        def res(i):
            if i == len(s):
                return True

            c = False
            for k in range(i+1, i+m+1):
                if s[i:k] in wordDict:
                    c = c or res(k)
            return c
        return res(0)



s = "leetcode"
wordDict = ["leet", "code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))

