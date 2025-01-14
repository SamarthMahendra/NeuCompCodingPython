class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero_count = [0] * n
        one_count = [0] * n

        # Precompute zero counts from the left
        zero_count[0] = 1 if s[0] == '0' else 0
        for i in range(1, n):
            zero_count[i] = zero_count[i - 1] + (1 if s[i] == '0' else 0)

        # Precompute one counts from the right
        one_count[n - 1] = 1 if s[n - 1] == '1' else 0
        for i in range(n - 2, -1, -1):
            one_count[i] = one_count[i + 1] + (1 if s[i] == '1' else 0)

        # Compute the maximum score by splitting at each position
        max_score = 0
        for i in range(n - 1):  # Ensure both substrings are non-empty
            max_score = max(max_score, zero_count[i] + one_count[i + 1])

        return max_score
