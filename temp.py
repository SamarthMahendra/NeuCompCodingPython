from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]

        def dfs(i, j, index):
            if index == len(word):
                return True

            if board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = '#'
            flag = False
            for r, c in directions:
                i, j = i + r, j + c
                if 0 <= i < rows and 0 <= j < cols and board[i][j] != '#':
                    flag = flag or dfs(i, j, index + 1)

            board[i][j] = temp
            return flag

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False





obj = Solution()
print(obj.exist([["a"]], "a"))






