a = input()
n = len(a)
dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i-1] + int(a[i-1]))
    if i >= 2:
        dp[i] = max(dp[i], dp[i-2] + int(a[i-2:i]))

print(dp[n])