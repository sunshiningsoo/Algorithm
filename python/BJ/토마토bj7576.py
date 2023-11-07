import sys

input = sys.stdin.readline
from collections import deque

col, row = map(int, input().split())

world = []
q = deque()
for i in range(row):
    world.append(list(map(int, input().split())))
    for j in range(col):
        if world[i][j] == 1:
            q.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

day = 1
isVisited = [[0 for _ in range(col)] for _ in range(row)]

def bfs():
    while q:
        popElement = q.popleft()
        x = popElement[0]
        y = popElement[1]
        isVisited[x][y] = 1
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < row and 0 <= yy < col:
                # if isVisited[xx][yy] or world[xx][yy] == -1:
                #     continue
                if isVisited[xx][yy] == 0 and world[xx][yy] == 0:
                    world[xx][yy] = world[x][y]+1
                    isVisited[xx][yy] = 1
                    q.append([xx, yy])

bfs()

for i in world:
    if 0 in i:
        print(-1)
        exit(0)
    day = max(max(i), day)

print(day-1)
    
        