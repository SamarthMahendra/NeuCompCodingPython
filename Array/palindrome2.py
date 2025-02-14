class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_palindrome_range(l + 1, r) or is_palindrome_range(l, r - 1)
            l, r = l + 1, r - 1
        return True


