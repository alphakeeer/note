
narr = input()
marr = input()
n = len(narr)
m = len(marr)

if n > m:
    n, m, narr, marr = m, n, marr, narr

# 直接用最长序列长-最长公共序列长 6AC 4WA
# def solution(n, m, narr, marr):  # n<m
#     dp = [0 for _ in range(m+1)]
#     for i in range(1, m+1):
#         tmp = dp[0]
#         for j in range(1, n+1):
#             if marr[i-1] == narr[j-1]:
#                 tmp, dp[j] = dp[j], tmp+1
#             else:
#                 tmp = dp[j]
#                 dp[j] = max(tmp, dp[j-1])
#     return m-dp[n]

#dp方程：dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
#dp[i][j]表示narr[:i]和marr[:j]达成相同所需要的最小操作数
def solution(n, m, narr, marr):
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]  # 0~n 0~m
    for i in range(m+1):
        if i <= n:
            dp[i][0] = i
        dp[0][i] = i
    for i in range(1, n+1):
        for j in range(1, m+1):
            if narr[i-1] == marr[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    return dp[n][m]


print(solution(n, m, narr, marr))
