class Solution(object):
    def rob(self, nums):
        if len(nums) == 1 :
            return nums[0]
        if len(nums) == 2 :
            return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        nums_len = len(nums)
        
        for n in range(2,nums_len) :
            for k in range(2,n+1) :
                dp[n] = max(dp[n-1],dp[n-k]+nums[n],dp[n])
        print(dp)
        return dp[-1]
        