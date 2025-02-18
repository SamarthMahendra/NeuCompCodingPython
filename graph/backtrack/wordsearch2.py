class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class TrieNode:

            def __init__(self):
                self.children = {}
                self.is_end = False

        class Trie:

            def __init__(self):
                self.root = TrieNode()

            def add(self, word):
                cur = self.root
                for w in word:
                    if w not in cur.children:
                        cur.children[w] = TrieNode()
                    cur = cur.children[w]
                cur.is_end = True
                return

        trie = Trie()
        for w in words:
            trie.add(w)

        n, m = len(board), len(board[0])

        res = set()

        def dfs(i, j, root, cur):
            if root.is_end:
                root.is_end = False
                res.add(cur)

            if not (0 <= i < n and 0 <= j < m) or board[i][j] not in root.children:
                return

            temp = board[i][j]
            board[i][j] = '#'
            dfs(i - 1, j, root.children[temp], cur + temp)
            dfs(i, j - 1, root.children[temp], cur + temp)
            dfs(i + 1, j, root.children[temp], cur + temp)
            dfs(i, j + 1, root.children[temp], cur + temp)
            board[i][j] = temp
            return

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie.root, '')
        return list(res)










