class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):
            window = s[i:i + total_len]
            window_words = [window[j:j + word_len] for j in range(0, total_len, word_len)]
            window_count = Counter(window_words)

            if window_count == word_count:
                result.append(i)

        return result











