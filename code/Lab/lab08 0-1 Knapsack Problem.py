n, w = map(int, input().split())
dp = [0 for _ in range(w+1)]
for i in range(n):
    val, wei = map(int, input().split())
    for j in range(w, wei-1, -1):
        dp[j] = max(dp[j], dp[j-wei]+val)
print(dp[w])
