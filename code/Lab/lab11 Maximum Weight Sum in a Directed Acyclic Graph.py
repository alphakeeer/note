'''
不会python的快速读数据
建议用C++
'''
n = int(input())  # node数目
wei = [0] + list(map(int, input().split()))
m = int(input())  # edge数目

ans=0
dp=[i for i in wei]
for i in range(m):
    a, b = map(int, input().split())
    if dp[b]<dp[a]+wei[b]:
        dp[b]=dp[a]+wei[b]
        if ans<dp[b]:
            ans=dp[b]
print(ans)


# import queue

# n = int(input())  # node数目
# g = [[] for _ in range(n+1)]
# wei = [0] + list(map(int, input().split()))
# m = int(input())  # edge数目
# for i in range(m):
#     a, b = map(int, input().split())
#     g[a].append(b)


# def bfs(cur, g, wei, dp, vis):
#     que = queue.Queue()
#     que.put(cur)
#     while not que.empty():
#         cur = que.get()
#         vis.add(cur)
#         son = g[cur]
#         for i in son:
#             if dp[i] < wei[i]+dp[cur]:
#                 dp[i] = wei[i]+dp[cur]
#                 que.put(i)
#             else:
#                 continue
#     return dp, vis


# dp = [i for i in wei]
# vis = set()
# for i in range(1, n+1):
#     if i not in vis:
#         dp, vis = bfs(i, g, wei, dp, vis)

# print(max(dp))





