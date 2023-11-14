N = int(input())

dp = [[0 for _ in range(N+1)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[j][i] = dp[j+1][i-1]
        elif j == 9:
            dp[j][i] = dp[j-1][i-1]
        else:
            dp[j][i] = dp[j-1][i-1] + dp[j+1][i-1]

hap = 0
for i in range(10):
    hap += dp[i][-1]
    # print(dp[i])

print(hap%1000000000)
