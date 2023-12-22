N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

maxNum = max(arr)

dp = [0 for _ in range(maxNum+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxNum+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009



for i in arr:
    print(dp[i]%1_000_000_009)
    