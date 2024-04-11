n, w = map(int, input().split())
ckitems = []
dp = [0 for _ in range(w+1)]
for i in range(n):
    # cki means Complete Knapsack Items, 0 => not, 1 => yes
    val, wei, cki = map(int, input().split())
    if cki == 0:
        for j in range(w, wei-1, -1):
            dp[j] = max(dp[j], dp[j-wei]+val)
    else:
        ckitems.append([val, wei])

m = len(ckitems)
for i in range(w+1):
    for ckitem in ckitems:
        val, wei = ckitem[0], ckitem[1]
        for j in range(w,wei-1,-1):
            dp[j] = max(dp[j], dp[j-wei]+val)


print(dp[w])
