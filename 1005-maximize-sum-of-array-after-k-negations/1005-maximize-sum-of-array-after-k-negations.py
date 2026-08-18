class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        for j in range(k) :
            idx = nums.index(min(nums))
            nums[idx] *= -1
        return sum(nums)