n, m = map(int, input().split())
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))
# make sure n is shorter than m
if n > m:
    n, m, narr, marr = m, n, marr, narr
    
#from大佬的代码
#时间复杂度优化到 nlogn (实际上应该是4n+nlogn)
def solution(n,m,narr,marr):
    n, m = map(int, input().split())
    narr = list(map(int, input().split()))
    marr = list(map(int, input().split()))
    f = [0 for i in range(0, n + 1)]
    t = [0 for i in range(0, n + 1)]
    ls = []
    newB = []
    
    #过滤多余元素
    for i in range(0, m):
        if marr[i] > n: continue
        newB.append(marr[i])
    marr = newB

    #输出t[]表示b中元素在a中的位置
    for i in range(0, n):
        f[narr[i]] = i
    for i in range(0, n):
        t[i] = f[marr[i]]
    
    #通过二分查找输出最长递增子数列
    for i in range(0, n):
        if len(ls) == 0 or t[i] > ls[-1]: ls.append(t[i])
        else:
            l, r = 0, len(ls) - 1
            while l < r:
                mid = (l + r) // 2
                if ls[mid] >= t[i]: r = mid
                else: l = mid + 1
            ls[l] = t[i]
    print(len(ls))

#时间复杂度O(mn)还能优化？？？
#空间复杂度min(m,n)但10ac,5爆时间
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
#     return dp[n]

# print(solution(n, m, narr, marr))

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


