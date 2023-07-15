# https://www.acmicpc.net/problem/11055
N = int(input())
arr = list(map(int, input().split()))

dp = arr[:] # arr를 copy해서 dp에 넣어준 것

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
