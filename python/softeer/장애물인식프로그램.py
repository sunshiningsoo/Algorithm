# https://softeer.ai/practice/info.do?idx=1&eid=409

N = int(input())
obstacleMap = [list(map(int, input())) for _ in range(N)]
dxdy = [[0,1], [1,0], [0,-1], [-1,0]]
obstacles = []
isChecked = [[0 for _ in range(N)] for _ in range(N)]
count = 0

def dfs(row, col):
    for dx, dy in dxdy:
        if 0 <= row + dx < N and 0 <= col + dy < N:
            if isChecked[row + dx][col + dy] != 1 and obstacleMap[row + dx][col + dy]:
                isChecked[row + dx][col + dy] = 1
                global count
                count += 1
                dfs(row + dx, col + dy)

def check():
    for i in range(N):
        for j in range(N):
            if obstacleMap[i][j] and isChecked[i][j] != 1:
                isChecked[i][j] = 1
                dfs(i, j)
                global count
                obstacles.append(count)
                count = 0

check()
print(len(obstacles))
obstacles.sort()
for i in obstacles:
    print(i+1)
