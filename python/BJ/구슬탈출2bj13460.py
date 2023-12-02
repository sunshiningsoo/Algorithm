# 파란 구슬이 구멍에 들어가면 안됨
R, C = map(int, input().split())
world = []
rLoc = []
bLoc = []
targetLoc = []
answer = 1e9
isVisited = [[[[0 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]

for i in range(R):
    world.append(list(input()))
    for j in range(C):
        if world[i][j] == 'R':
            rLoc = [i, j]
        if world[i][j] == 'B':
            bLoc = [i, j]
        if world[i][j] == 'O':
            targetLoc = [i, j]

# 상하좌우 순
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mover(x, y, dir):
    count = 0
    while world[x + dx[dir]][y + dy[dir]] != '#' and world[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        count += 1
    return (x, y, count)


def dfs(current, rrLoc, bbLoc):
    global answer
    # answer += 1
    if current > 10:
        return
    isVisited[rrLoc[0]][rrLoc[1]][bbLoc[0]][bbLoc[1]] = 1
    for i in range(4):
        rxx, ryy, rmover = mover(rrLoc[0], rrLoc[1], i)
        bxx, byy, bmover = mover(bbLoc[0], bbLoc[1], i)

        if [bxx, byy] == targetLoc:
            continue
        if [rxx, ryy] == targetLoc:
            answer = min(answer, current)
            return
        if [rxx, ryy] == [bxx, byy]:
            if rmover > bmover:
                rxx -= dx[i]
                ryy -= dy[i]
            elif rmover < bmover:
                bxx -= dx[i]
                byy -= dy[i]
        if isVisited[rxx][ryy][bxx][byy] != 1:
            dfs(current + 1, [rxx, ryy], [bxx, byy])
            isVisited[rxx][ryy][bxx][byy] = 0


dfs(1, rLoc, bLoc)
if answer == 1e9:
    print(-1)
else:
    print(answer)