class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        smallest = min(strs, key=len)

        for i, char in enumerate(smallest):
            for s in strs:
                if char != s[i]:
                    return s[:i]
        return smallest

