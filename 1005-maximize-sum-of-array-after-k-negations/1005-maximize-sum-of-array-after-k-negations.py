class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()                       # 가장 작은(=가장 음수) 것부터
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:     # 음수를 양수로 (가장 이득)
                nums[i] = -nums[i]
                k -= 1
        total = sum(nums)
        if k % 2 == 1:                    # 남은 뒤집기가 홀수면
            total -= 2 * min(nums)        # 절댓값 최소 하나만 음수로
        return total