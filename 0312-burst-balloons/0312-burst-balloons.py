class Solution(object):
    def maxCoins(self,nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # 구간 길이 2부터 (풍선 1개) ~ n-1까지 (전체)
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + coins + dp[k][right]
                    )

        return dp[0][n - 1]