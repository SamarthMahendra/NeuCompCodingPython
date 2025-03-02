class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.is_end = False

        class Trie:

            def __init__(self):
                self.root = TrieNode()

            def put(self, word):
                cur = self.root

                for w in word:
                    if w not in cur.children:
                        cur.children[w] = TrieNode()
                    cur = cur.children[w]
                cur.is_end = True
                return

        trie = Trie()
        for word in words:
            trie.put(word)

        res = set()
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        rows, cols = len(board), len(board[0])

        def dfs(i, j, root, cur=''):
            if root.is_end:
                res.add(cur)

            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] not in root.children:
                return
            temp = board[i][j]
            board[i][j] = '#'

            for r, c in directions:
                ni, nj = i + r, j + c
                dfs(ni, nj, root.children[temp], cur + temp)

            board[i][j] = temp
            return

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root)

        return list(res)



