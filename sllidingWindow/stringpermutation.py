from collections import Counter



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Count the frequency of characters in s1
        s1_count = Counter(s1)
        window_count = Counter()

        for i, char in enumerate(s2):
            window_count[char] += 1

            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            if window_count == s1_count:
                return True

        return False




