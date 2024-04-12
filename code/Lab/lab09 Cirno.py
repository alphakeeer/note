n, l, r = map(int, input().split())
river = list(map(int, input().split()))

# dp第一维记录到达i点时的最大积分
# 用dp的第二维记录是否能达到，1为走过，0为无法到达
# AC13 WA1 TLE1


def solution(n, l, r, river):
    ans = 0
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = 1
    for i in range(n):
        if dp[i][1] == 0:  # 确保可行
            continue
        if i + l >= n:  # 到达终点
            if dp[i][0] > ans:
                ans = dp[i][0]
                continue
        for j in range(l, r + 1):  # 向前铺路
            if i + j >= n:  # 到达终点
                if dp[i][0] > ans:
                    ans = dp[i][0]
            # dp方程
            elif dp[i][0] + river[i + j] > dp[i + j][0] or dp[i + j][0] == 0:
                dp[i + j][0] = dp[i][0] + river[i + j]
                dp[i + j][1] = 1

    return ans


print(solution(n+1, l, r, river))
