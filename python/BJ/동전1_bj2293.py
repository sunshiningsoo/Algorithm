N, K = map(int, input().split())
coinList = []
for i in range(N):
    coinList.append(int(input()))

dp = [0] * (K+1)
dp[0] = 1



for coin in coinList:
    for j in range(coin, K+1, 1):
        # j원을 만족시키는 동전 갯수
        dp[j] = dp[j] + dp[j-coin] # 이전에 누적되어 있던 j 원에서 새로운 coin을 추가할때, j-coin 까지 누적되어 있던 경우의 수가 추가될 수 있음

# dp 테이블이 아래와 같이 업데이트 됨
# 1 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 2 [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
# 5 [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]

print(dp[K])

