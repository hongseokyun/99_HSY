class Solution(object):
    def jump(self, nums):
        jump = {i: i + c for i, c in enumerate(nums)}
        step = 0          # 지금까지 도달 가능한 '가장 먼' 지점
        cur_end = 0       # ★ 추가: 현재 점프로 닿을 수 있는 경계
        cnt = 0
        for i in range(len(nums) - 1):   # ★ 마지막 칸 직전까지만 (이미 도착이면 0)
            if jump[i] > step:
                step = jump[i]           # 도달 범위 갱신
            if i == cur_end:             # ★ 현재 점프의 끝에 도달 → 한 번 점프
                cnt += 1
                cur_end = step           # 다음 점프의 경계 = 지금까지의 최대 도달
        return cnt