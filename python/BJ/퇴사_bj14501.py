N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

dp = [[world[i][0], 0] for i in range(N)]
for i in range(N):
    if world[i][0] + i <= N:
        dp[i][1] = world[i][1]

for i in range(1, len(world)):
    for j in range(i):
        if j + world[j][0] <= i and i + world[i][0] <= N:
            dp[i][1] = max(dp[i][1], dp[j][1] + world[i][1])

dp.sort(key=lambda x: x[1])
print(dp[-1][-1])
