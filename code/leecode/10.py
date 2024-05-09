class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s)+1, len(p)+1
        dp = [[False]*n for _ in range(m)]   # dp[s][p]
        # 初始化
        dp[0][0] = True
        for i in range(2, n, 2):
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'
        # dp过程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-2] or dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.') \
                    if p[j-1] == '*' else \
                    dp[i-1][j-1] and (p[j-1] == '.' or s[i-1] == p[j-1])

        return dp[-1][-1]
