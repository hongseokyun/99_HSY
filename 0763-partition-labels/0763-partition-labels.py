class Solution(object):
    def partitionLabels(self, s):
        last = {c: i for i, c in enumerate(s)}   # 각 글자의 마지막 인덱스
        result = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])   # 현재 구간이 최소 여기까지는 가야 함
            if i == end:              # 구간 안 모든 글자의 마지막까지 왔으면
                result.append(end - start + 1)
                start = i + 1
        return result