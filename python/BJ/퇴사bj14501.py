N = int(input())

T = [0] # 몇일 걸리는지
P = [0] # 얼마인지
dp = [0]
for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)
    dp.append(b)

dp[1] = P[1]
dp.append(0)
for i in range(N, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[1])
