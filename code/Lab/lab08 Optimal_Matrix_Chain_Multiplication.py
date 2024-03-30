import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

# 尝试dp again
# AC14 TLE16
# 时间复杂度O(n^3)
# 空间复杂度O(n^2)


def solution(n, nums):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for length in range(2, n+1):  # 遍历矩阵组的长度
        for i in range(n-length+1):  # 遍历初始点
            j = i+length-1  # 末点
            dp[i][j] = float("inf")
            a = nums[i]*nums[j+1]
            for k in range(i, j):  # 划分
                cur = dp[i][k]+dp[k+1][j]+a*nums[k+1]
                # dp[i][j] = min(dp[i][j], cur)
                if dp[i][j] > cur:
                    dp[i][j] = cur
    return dp[0][n-1]


print(solution(n, nums))

# ans = float("inf")
# 直接递归全红TLE
# def solution(nums, scalar):
#     global ans
#     l = len(nums)
#     if l == 3:
#         cur = nums[0]*nums[1]*nums[2]
#         scalar += cur
#         ans = min(ans, scalar)
#         return
#     for i in range(1, l-1):
#         cur = nums[i-1]*nums[i+1]*nums[i]
#         arr = nums[:i]+nums[i+1:]
#         solution(arr, scalar+cur)
# solution(nums,0)

# 尝试dp，结果内存和时间都爆了
# def solution(n, nums):
#     dp = [{} for _ in range(n+1)]
#     # n
#     for i in range(1, n):
#         cur = nums[i]*nums[i-1]*nums[i+1]
#         dp[n][(i,)] = cur
#     # n-1
#     for m in range(n, 2, -1):
#         for key, val in dp[m].items():
#             for i in range(1, m-1):
#                 if i not in key:
#                     new_key = key + (i,)
#                     j, k = i-1, i+1
#                     while k in new_key:
#                         k += 1
#                     while j in new_key:
#                         j -= 1
#                     cur = nums[i]*nums[j]*nums[k]
#                     if new_key not in dp[m-1]:
#                         dp[m-1][new_key] = cur+val
#                     else:
#                         dp[m-1][new_key] = min(dp[m-1][new_key], cur+val)
#     for val in dp[2].values():
#         print(val)
# solution(n, nums)
