N = int(input())
dp = [[]] * (N+1)
temp = N
dp[1] = [1]

for i in range(2, N+1):
    dp[i] = dp[i-1] + [i]
    if i % 2 == 0:
        if len(dp[i//2]) + 1 < len(dp[i]):
            dp[i] = dp[i//2] + [i]
    if i % 3 == 0:
        if len(dp[i // 3]) + 1 < len(dp[i]):
            dp[i] = dp[i // 3] + [i]



print(len(dp[-1])-1)
print(*dp[-1][::-1])