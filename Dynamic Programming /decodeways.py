class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def res(i):
            if i == len(s):
                return 1

            if i > len(s):
                return 0

            count = 0
            if int(s[i]) != 0:
                count += res(i + 1)
            if int(s[i:i + 2]) <= 26 and s[i] != '0':
                count += res(i + 2)
            return count

        return res(0)

