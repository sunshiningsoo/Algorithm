import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())

world = []
sharks = deque([])
for i in range(R):
    world.append(list(map(int, input().split())))
    for j in range(C):
        if world[i][j] == 1:
            sharks.append([i, j, 0])
        else:
            world[i][j] = 1e9

dir = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

while sharks:
    x, y, cnt = sharks.popleft()
    for dx, dy in dir:
        nx = x+dx
        ny = y+dy
        if 0<=nx<R and 0<=ny<C and world[nx][ny] > cnt + 1: # 여기서 cnt+1이 아니고 cnt 만 하면 동일한 cell 체크를 계속해서 시간초ㅎ과임
            world[nx][ny] = cnt+1
            sharks.append([nx, ny, cnt+1])

answer = 0
for i in world:
    answer = max(answer, max(i))
print(answer)
