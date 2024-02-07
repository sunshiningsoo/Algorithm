import sys
input = sys.stdin.readline
N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))
dp = [0 for _ in range(N+1)]
world.insert(0, [0, 0])

for i in range(1, N+1):
    # 이전까지의 최대와 현재 저장된 최대(if 문에서 들어온 값)를 비교
    dp[i] = max(dp[i-1], dp[i])
    # 당일 허용
    nxt = i + world[i][0] - 1
    if nxt <= N:
        # 타겟의 최댓값과 이전까지 + 현재
        dp[nxt] = max(dp[nxt], dp[i-1] + world[i][1])

    print(i, nxt, dp)

print(dp[-1])
