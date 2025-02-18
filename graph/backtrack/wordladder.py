from collections import deque


def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)  # Convert wordList to a set for O(1) lookup
    if endWord not in wordSet:
        return 0  # If endWord is not in wordList, there's no possible transformation

    queue = deque([(beginWord, 1)])  # (current_word, transformation_length)

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length  # Found the shortest transformation

        # Try changing each letter in the word
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]

                if new_word in wordSet:
                    queue.append((new_word, length + 1))
                    wordSet.remove(new_word)  # Mark as visited by removing from wordSet

    return 0  # If no path found



