class Solution(object):
    def canJump(self, nums):
        jump = {i: i + c for i, c in enumerate(nums)}
        object_step = len(nums) - 1
        step = 0                       # 지금까지 도달 가능한 '가장 먼' 지점
        for i in range(len(nums)):
            if i > step:               # ★ 추가: 이 칸조차 못 밟으면 즉시 실패
                return False
            if jump[i] > step:         # ★ 이중 루프 대신, 현재 칸의 jump[i]로 갱신
                step = jump[i]
        return step >= object_step     # ★ == → >=