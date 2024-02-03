R, C = map(int, input().split())

world = []
jStart = []
FStart = []
fireVisited = [[0 for _ in range(C)] for _ in range(R)]
isVisited = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    world.append(list(input()))
    for j in range(C):
        if world[i][j] == 'J':
            jStart.append([i, j])
            isVisited[i][j] = 1
        if world[i][j] == 'F':
            FStart.append([i, j])
            fireVisited[i][j] = 1

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
checker = False

while True:
    answer += 1
    fireSpread = FStart.copy()
    FStart = []

    while fireSpread:
        x, y = fireSpread.pop(0)
        fireVisited[x][y] = 1
        world[x][y] = 'F'
        for dx, dy in dir:
            nx = dx+x
            ny = dy+y
            if 0<=nx<R and 0<=ny<C and fireVisited[nx][ny] == 0 and world[nx][ny] != '#':
                fireVisited[nx][ny] = 1
                world[nx][ny] = 'F'
                FStart.append([nx, ny])

    jSpread = jStart.copy()
    jStart = []

    while jSpread:
        x, y = jSpread.pop(0)
        isVisited[x][y] = 1
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            checker = True
            break
        for dx, dy in dir:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < R and 0 <= ny < C and isVisited[nx][ny] == 0 and \
                world[nx][ny] == '.' and fireVisited[nx][ny] == 0:

                isVisited[nx][ny] = 1
                if nx == 0 or nx == R-1 or ny == 0 or ny == C-1:
                    checker = True
                    answer += 1
                    break

                jStart.append([nx, ny])
        if checker:
            break

    if checker:
        break
    if len(jStart) == 0:
        break


if checker:
    print(answer)
else:
    print("IMPOSSIBLE")

