import sys
input = sys.stdin.readline
N = int(input())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

# 1이 비숍 놓을 수 있는 곳
dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

isVisited = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

def in_range(x, y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def isVisitedCheck(x, y, flag):
    if flag:
        isVisited[x][y] += 1
        q = []
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                isVisited[nx][ny] += 1
                q.append([nx, ny, dx, dy])
        while q:
            cx, cy, dx, dy = q.pop(0)
            nx, ny = cx+dx, cy+dy
            if in_range(nx, ny):
                isVisited[nx][ny] += 1
                q.append([nx, ny, dx, dy])
    else:
        isVisited[x][y] -= 1
        q = []
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                isVisited[nx][ny] -= 1
                q.append([nx, ny, dx, dy])
        while q:
            cx, cy, dx, dy = q.pop(0)
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny):
                isVisited[nx][ny] -= 1
                q.append([nx, ny, dx, dy])


def back(x, y, cnt, flag):
    global answer
    if cnt > answer:
        answer = max(answer, cnt)

    for i in range(x, N):
        cur = 0
        if i == x:
            cur = y
        for j in range(cur, N):
            if flag:
                if i%2==0 and j%2==1: continue
                if i % 2 == 1 and j % 2 == 0: continue
                if isVisited[i][j] == 0 and world[i][j] == 1:
                    isVisitedCheck(i, j, True)
                    back(i, j, cnt + 1, flag)
                    isVisitedCheck(i, j, False)
            else:
                if i%2==0 and j%2==0: continue
                if i % 2 == 1 and j % 2 == 1: continue
                if isVisited[i][j] == 0 and world[i][j] == 1:
                    isVisitedCheck(i, j, True)
                    back(i, j, cnt + 1, flag)
                    isVisitedCheck(i, j, False)


for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            if i % 2 == 0 and j % 2 == 1: continue
            if i % 2 == 1 and j % 2 == 0: continue
            back(i, j, 0, True)
temp = answer
# print(answer)
answer = 0

for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            if i % 2 == 0 and j % 2 == 0: continue
            if i % 2 == 1 and j % 2 == 1: continue
            back(i, j, 0, False)

print(answer+temp)
