# https://www.acmicpc.net/problem/11053
N = int(input())
arr = list(map(int, input().split()))
answer = 1

# for i in range(0, len(arr)-1):
#     current = arr[i]
#     temp = 1
#     for j in range(i+1, len(arr)):
#         if current < arr[j]:
#             current = arr[j]
#             temp += 1
#
#     answer = max(answer, temp)
#
# print(answer)

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))
