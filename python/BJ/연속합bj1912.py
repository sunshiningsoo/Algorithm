N = int(input())

arr = list(map(int, input().split()))
dp = [0] * (N+1)
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(arr[i], arr[i]+dp[i-1])
    # 점화식을 생각하면됨
dp[-1] = -1001
print(max(dp))
