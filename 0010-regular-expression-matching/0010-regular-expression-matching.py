class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # 빈 문자열 vs 빈 패턴

        # 빈 문자열 s에 대해 "a*b*c*" 같은 패턴이 매칭 가능
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * 앞의 문자를 0개 사용: dp[i][j-2]
                    # * 앞의 문자를 1개 이상 사용: s[i-1]이 매칭되고 dp[i-1][j]
                    dp[i][j] = dp[i][j - 2] or \
                               (dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.'))
                else:
                    # 현재 문자가 일치하면 이전 상태 계승
                    dp[i][j] = dp[i - 1][j - 1] and \
                               (p[j - 1] == s[i - 1] or p[j - 1] == '.')

        return dp[m][n]