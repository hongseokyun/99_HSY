from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS: 레벨별로 탐색하며 부모 기록
        parents = defaultdict(set)  # word -> 이전 단어들
        current_level = {beginWord}
        found = False

        while current_level and not found:
            # 이번 레벨 단어들은 이후 레벨에서 재방문 금지
            wordSet -= current_level
            next_level = set()
            for word in current_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            next_level.add(newWord)
                            parents[newWord].add(word)
            if endWord in next_level:
                found = True
            current_level = next_level

        # 역추적으로 경로 복원
        if not found:
            return []

        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(list(reversed(path)))
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        backtrack(endWord, [endWord])
        return res