class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(o, c, cur=''):
            if o == n == c:
                res.append(cur)

            else:
                if o < n:
                    backtrack(o + 1, c, cur + '(')
                if c < o:
                    backtrack(o, c + 1, cur + ')')

            return

        backtrack(0, 0)
        return res

