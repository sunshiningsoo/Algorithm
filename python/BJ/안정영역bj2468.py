import sys
sys.setrecursionlimit(100000)
N = int(input())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

maxH = 0
for i in range(N):
    maxH = max(maxH, max(world[i]))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dap = 0

def dfs(currentRow, currentCol, h):
    global dap
    isVisited[currentRow][currentCol] = 1
    for i in range(4):
        dxx = dx[i] + currentRow
        dyy = dy[i] + currentCol
        if 0<= dxx < N and 0<= dyy < N and isVisited[dxx][dyy] == 0 and world[dxx][dyy] > h:
            dfs(dxx, dyy, h)

sample = []
isVisited = [[0 for _ in range(N)] for _ in range(N)]

for h in range(0, maxH+1):
    isVisited = [[0 for _ in range(N)] for _ in range(N)]
    dap = 0
    for i in range(N):
        for j in range(N):
            if isVisited[i][j] == 0 and world[i][j] > h:
                dfs(i, j, h)
                dap += 1
    sample.append(dap)


print(max(sample))
