class Solution(object):
    def subsets(self,nums):
        res = []
        def backtrack(start, path):
            res.append(path[:])          # 현재 조합을 결과에 추가 (모든 노드가 정답)
            for i in range(start, len(nums)):
                path.append(nums[i])     # 선택
                backtrack(i + 1, path)   # 다음 원소부터 탐색
                path.pop()               # 선택 취소 (백트래킹!)
        backtrack(0, [])
        return res