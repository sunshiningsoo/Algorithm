import sys
input = sys.stdin.readline
# 시간 초과가 나올 경우 sys를 사용해 시간을 줄여보자

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 시간 초과 풀이법
# ans = []
# for k in range(M):
#     i, j = map(int, input().split())
#     ans.append(sum(arr[i-1:j]))
#
# for k in ans:
#     print(k)


dp = [0]*(N+1)
for k in range(N):
    dp[k+1] = dp[k] + arr[k]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])

