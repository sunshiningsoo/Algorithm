n = int(input())

dp = [0] * (100001)

# 2, 5
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 2
dp[5] = 1
# [0, 0, 1, 0, 2, 1, 3, ]
if n <= 5:
    if n==1 or n==3:
        print(-1)
    else:
        print(dp[n])
    exit(0)
else:
    for i in range(6, n+1):
        if dp[i-5] != 0 and dp[i-2] != 0:
            dp[i] = min(dp[i-5], dp[i-2]) + 1
        elif dp[i-5] == 0:
            dp[i] = dp[i-2]+1
        elif dp[i-2] == 0:
            dp[i] = dp[i-5] + 1


if dp[n] != 0:
    print(dp[n])
else:
    print(-1)
