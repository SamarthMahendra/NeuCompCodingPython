class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        text1 = s
        text2 = s[::-1]
        dp = [[0] * (n + 1) for i in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]




