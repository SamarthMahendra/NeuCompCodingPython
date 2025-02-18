class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True

            if not (0 <= i < n and 0 <= j < m) or word[index] != board[i][j]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            res = dfs(i + 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j - 1,
                                                                                                          index + 1)
            board[i][j] = temp
            return res

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

