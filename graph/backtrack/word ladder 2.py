class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookup
        if endWord not in wordSet:
            return []  # If endWord is not in wordList, there's no possible transformation

        queue = deque([(beginWord, [beginWord])])  # (current_word, transformation_length)
        res = []
        level_visited = set()
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                word, path = queue.popleft()
                if word == endWord:
                    res.append(path)
                    found = True  # Mark found but don't break yet

                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in wordSet:
                            queue.append((new_word, path + [new_word]))
                            level_visited.add(new_word)  # Store words for removal after level

            wordSet -= level_visited

        return res

