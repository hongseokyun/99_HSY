class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        child = 0   # 현재 만족시키려는 아이 인덱스
        for cookie in s:
            if child < len(g) and g[child] <= cookie:
                child += 1   # 이 아이 만족 → 다음 아이로
        return child