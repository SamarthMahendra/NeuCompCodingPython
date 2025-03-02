class TrieNode:

    def __init__(self):
        self.children = {}
        self.isend = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.isend = True
        return

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return cur.isend

            if word[i] == '.':
                for k, c in cur.children.items():
                    if dfs(c, i + 1):
                        return True
            elif word[i] in cur.children:
                return dfs(cur.children[word[i]], i + 1)
            else:
                return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)