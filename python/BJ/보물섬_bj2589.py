from collections import deque

R, C = map(int, input().split())
world = []
for i in range(R):
    world.append(list(input()))

isVisited = [[0 for _ in range(C)] for _ in range(R)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

def check(x, y):
    global ans
    q = deque()
    q.append([x, y, 0])
    isVisited[x][y] = 1


    while q:
        cx, cy, cnt = q.popleft()
        ans = max(ans, cnt)
        for dx, dy in dirs:
            nx = cx + dx
            ny = cy + dy
            if 0<= nx < R and 0 <= ny <C:
                if world[nx][ny] == 'L' and isVisited[nx][ny] == 0:
                    isVisited[nx][ny] = 1
                    q.append([nx, ny, cnt + 1])
    # if [x, y] == [3, 0]:
    #     print(ans)

def isVisitedClear():
    global isVisited
    isVisited = [[0 for _ in range(C)] for _ in range(R)]


for i in range(R):
    for j in range(C):
        if world[i][j] == 'L':
            isVisitedClear()
            check(i, j)

print(ans)
