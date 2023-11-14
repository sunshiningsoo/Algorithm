# https://www.acmicpc.net/board/view/60664 이전까지 마신 최댓값을 포함해줘야 하는 이유
N = int(input())

podo = [int(input()) for _ in range(N)]
podo.insert(0, 0)

dp = [0] * 10001
if N == 1 or N == 2:
    print(sum(podo))
    exit(0)
dp[1] = podo[1]
dp[2] = podo[1] + podo[2]
dp[3] = max(podo[1] + podo[3], podo[2] + podo[3], dp[2])

for i in range(3, N+1):
    dp[i] = max(podo[i-1] + dp[i-3] + podo[i], dp[i-2] + podo[i], dp[i-1])

print(max(dp))

# 3일연속은 불가능

# 오늘-3 오늘-2 오늘-1 오늘

# dp[i] = max(podo[i-1] + dp[i-3], dp[i-2]) + podo[i] 와
# dp[i] = max(podo[i-1] + dp[i-3] + podo[i], dp[i-2] + podo[i], dp[i-1]) 두개의 차이는 뭐지..

