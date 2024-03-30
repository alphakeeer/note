n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))
# make sure n is shorter than m
if n > m:
    n, m, narr, marr = m, n, marr, narr
    
#空间复杂度min(m,n)但10ac,5爆时间
def solution(n, m, narr, marr):  # n<m
    dp = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        tmp = dp[0]
        for j in range(1, n+1):
            if marr[i-1] == narr[j-1]:
                tmp, dp[j] = dp[j], tmp+1
            else:
                tmp = dp[j]
                dp[j] = max(tmp, dp[j-1])
    return dp[n]

print(solution(n, m, narr, marr))

#dp思路
# dp=[n][m]
# if n[i]=m[j]:dp[i][j]=dp[i-1][j-1]+1
# else dp[i][j]=max(dp[i][j-1],dp[i-1][j])
#ac10，5内存和时间都爆
# def solution(n, m, narr, marr):
#     dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if narr[i-1] == marr[j-1]:
#                 dp[i][j] = dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#     return dp[n][m]




# 3 5
# 1 2 3 4
# 1 4 2 5 3
# 1 2 2 0 3

# def find(l, narr,n):
#     for i in range(n):
#         if l[i] == narr:
#             return i
#     return -1


# def solution(n, m, narr, marr):
#     dp = [0 for _ in range(m+1)]
#     for i in range(1, m+1):
#         idx1 = find(narr, marr[i-1],n)
#         if idx1 != -1:
#             dp[i] = 1
#             for j in range(1, i+1):
#                 idx2 = find(narr, marr[j-1],idx1)
#                 if idx2 != -1:
#                     dp[i] = max(dp[j]+1, dp[i])
#     ans = 0
#     for i in range(1, m+1):
#         ans = max(ans, dp[i])
#     print(int(ans))


