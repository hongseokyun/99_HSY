class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        queue = [0]          # 시작 인덱스
        visited = set()

        while queue:
            start = queue.pop(0)
            if start == len(s):
                return True
            if start in visited:
                continue
            visited.add(start)
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words:
                    queue.append(end)
        return False