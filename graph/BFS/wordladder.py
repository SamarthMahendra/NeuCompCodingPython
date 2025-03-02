class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if beginWord == endWord:
            return 0
        queue = deque([(beginWord, 0)])

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step + 1

            for i in range(len(endWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + c + word[i + 1:]
                    if newword in wordList:
                        queue.append((newword, step + 1))
                        wordList.remove(newword)
        return 0







