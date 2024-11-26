class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmasks = []
        lengths = []

        for word in words:
            bitmask = 0
            for char in word:
                bitmask = bitmask | 1 << (ord(char) - ord('a'))
            bitmasks.append(bitmask)
            lengths.append(len(word))
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_product = max(
                        max_product, lengths[i] * lengths[j]
                    )
        return max_product

