class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        m = max(map(len, wordDict))

        def dfs(i):
            if i == len(s):
                return True
            res = False
            for k in range(i + 1, min(i + m + 1, len(s) + 1)):
                if s[i:k] in wordDict:
                    res = res or dfs(k)
            return res

        return dfs(0)






