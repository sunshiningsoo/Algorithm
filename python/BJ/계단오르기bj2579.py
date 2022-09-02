N = int(input())

# arr의 크기 초기화가 되어 있어야 runtime error를 피할 확률이 높다.
arr = [0]*300

for i in range(N):
    arr[i] = int(input())

dp = [0] * 300
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = (max(arr[0], arr[1])) + arr[2]
for k in range(3, N):
    dp[k] = (max(dp[k-3] + arr[k-1], dp[k-2])) + arr[k]

print(dp[N-1])

#################

# n = int(input())
#
# graph = [0]*300
# for i in range(n):
#     graph[i] = int(input())
#
# dp = [0]*300
# dp[0] = graph[0]
# dp[1] = graph[0]+graph[1]
# dp[2] = graph[2]+(max(graph[0], graph[1]))
#
# for i in range(3, n):
#     dp[i] = max(dp[i-2]+graph[i], dp[i-3]+graph[i-1]+graph[i])
#
# print(dp[n-1])
