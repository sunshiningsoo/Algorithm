import sys
input = sys.stdin.readline
N, M = map(int, input().split())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

nuzuk = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        nuzuk[i][j] = nuzuk[i][j-1] + world[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    temp = 0
    for i in range(x1, x2+1):
        temp += nuzuk[i][y2] - nuzuk[i][y1-1]
    print(temp)




