class Solution(object):
    def fib(self, n):
        if n == 0 :
            return 0
        if n <= 2 :
            return 1
        dp = [0,1] + [0]*(n-1)

        for i in range(n-1) :
            dp[i+2] = dp[i+1] + dp[i]

        return dp[-1]