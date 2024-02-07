N = int(input())
dp = [[1, 1] for _ in range(N)]
dp[0] = [2, 2]
for i in range(2, N):
    dp[i][0] = 2 * (dp[i-2][0] + dp[i-2][1])
    dp[i][1] = 2 * (dp[i-2][0] + dp[i-2][1])

print(dp[-1])

# 9901로 나눈 나머지를 출력해야됨
