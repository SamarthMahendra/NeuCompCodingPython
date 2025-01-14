from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Edge cases
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # If we've matched all characters in word
            if index == len(word):
                return True

            # Out of bounds or mismatch, return False
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # Temporarily mark the cell as visited by changing the character
            temp = board[r][c]
            board[r][c] = '#'  # or some special marker

            # Explore the 4 possible directions
            found = (
                    dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1)
            )

            # Restore the character (backtrack)
            board[r][c] = temp

            return found

        # Try every cell as a possible starting point
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # optional early check
                    if dfs(i, j, 0):
                        return True
        return False