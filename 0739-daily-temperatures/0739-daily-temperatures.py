class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  # 아직 더 따뜻한 날을 못 찾은 인덱스들
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        return result