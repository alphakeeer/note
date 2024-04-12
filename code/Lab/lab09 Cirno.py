from collections import deque

def solution(n, l, r, river):
    # dp记录到达i点时的最大积分
    dp = [float('-inf')] * (n)  # dp初始化为最小方便比较最大值
    dp[0] = 0       # 起始位置积分为0，非('-inf')即表示可达
    dq = deque([0])   # 双端列表，用于作为滑窗记录最大数的index

    '''
    思路与原理：
    dp[i]为到达该点i时的最大积分
    正常状态转移方程应为：
        dp[i]=max(dp[i-r:i-l])+river[i] #即在步长范围内(i-r,i-l)的最大值加上该点i的积分
    这个操作时间复杂度看似O(n),实则为Θ(n*(r-l))
    为进一步减小时间复杂度,考虑使用"移动滑窗最大值"
    其操作原理详见 https://www.cxyxiaowu.com/14367.html
    可以做到O(1)时间内获得步长范围内(i-r,i-l)的最大值
    具体为使用deque双端列表的dq[0]记录最大值的index,达到更简单的状态转移方程
        dp[i]=river[i]+dp[dq[0]]
    '''
    for i in range(l, n):  # 从l处开始遍历（因为是从i处向(i-r,i-l)得到数据）

        dp[i] = river[i]+dp[dq[0]]  # 状态转移方程，dq默认为0

        # 为下一个i维护dq
        while dq and dq[0] < i-r+1:  # 当index超出范围i-r+1时排除
            dq.popleft()
        while dq and dp[dq[-1]] <= dp[i-l+1]:  # 推出小于当前值的index
            dq.pop()
        dq.append(i-l+1)  # 推入当前值的index

    ans = max(dp[i] for i in range(n - r, n))  # ans为后能直接到达终点的最大值

    return ans

#数据读入处理
n, l, r = map(int, input().split())
river = list(map(int, input().split()))
print(solution(n+1, l, r, river))

# 以下是做题历史尝试，可忽略

# dp第一维记录到达i点时的最大积分
# 用dp的第二维记录是否能达到，1为走过，0为无法到达
# AC13 WA1 TLE1
# def solution(n, l, r, river):
#     ans = 0
#     dp = [[0, 0] for _ in range(n)]
#     dp[0][1] = 1
#     for i in range(n):
#         if dp[i][1] == 0:  # 确保可行
#             continue

#         for j in range(l, r + 1):  # 向前铺路
#             if i + j >= n:  # 到达终点
#                 if dp[i][0] > ans:
#                     ans = dp[i][0]
#                 break
#             # dp方程
#             elif  dp[i + j][0] == 0 or dp[i][0] + river[i + j] > dp[i + j][0]:
#                 dp[i + j][0] = dp[i][0] + river[i + j]
#                 dp[i + j][1] = 1

#     return ans

# def solution(n, l, r, river):
#     # dp记录到达i点时的最大积分
#     # dp初始化为最小
#     dp = [float('-inf')] * (n)
#     dp[0] = 0  # 起始位置积分为0，非('-inf')即表示起点可达

#     for i in range(n):
#         if dp[i] == float('-inf'):  # 确保可行
#             continue

#         for j in range(l, r + 1):   # 向前铺路
#             if i + j < n:
#                 if dp[i+j] < dp[i] + river[i + j]:
#                     dp[i+j] = dp[i] + river[i + j]

#     # 查找可到达终点的最大积分
#     ans = max(dp[i] for i in range(n - r, n))

#     return ans


# def fun(li, n, l, r):
#     ans = [0 for i in range(len(li))]
#     for i in range(len(ans)):
#         ans[i] = float('-inf') if i != 0 else 0
#         if i-l < 0:
#             continue
#         elif i-l >= 0 and i-r < 0:
#             for j in range(i-l+1):
#                 if ans[i] < ans[j]+li[i]:
#                     ans[i] = ans[j]+li[i]
#         elif i-r >= 0:
#             for j in range(i-r, i-l+1):
#                 if ans[i] < ans[j]+li[i]:
#                     ans[i] = ans[j]+li[i]
#     return ans


# n, l, r = map(int, input().split())
# li = list(map(int, input().split()))
# ans = fun(li, n, l, r)
# result = 0
# for i in range(len(ans)-r, len(ans)):
#     result = max(result, ans[i])
# print(result)
