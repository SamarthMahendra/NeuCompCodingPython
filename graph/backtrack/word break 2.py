class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)

        @lru_cache(maxsize=None)
        def dfs(start: int) -> List[str]:
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub_sentence in dfs(end):
                        sentences.append(word + ("" if sub_sentence == "" else " " + sub_sentence))
            return sentences

        return dfs(0)
