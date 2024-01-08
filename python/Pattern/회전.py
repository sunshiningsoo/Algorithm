N = 7
world = [[0 for _ in range(N)] for _ in range(N)]

r = N // 2
c = N // 2

#     상  좌  하  우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

isVisited = [[0 for _ in range(N)] for _ in range(N)]
isVisited[r][c] = 1
dir = 0
cnt = 1

while [r, c] != [0, 0]:
    dir = (dir+1) % 4
    nr = r + dx[dir]
    nc = c + dy[dir]
    if isVisited[nr][nc] == 1:
        dir -= 1
        if dir < 0:
            dir = 3
        nr = r + dx[dir]
        nc = c + dy[dir]

    world[nr][nc] = cnt
    isVisited[nr][nc] = 1
    cnt += 1
    r, c = nr, nc

for i in world:
    print(*i)
print()


