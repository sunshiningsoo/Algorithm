from collections import deque

test_case = int(input())
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(test_case):
    R, C = map(int, input().split())
    R, C = C, R
    world = []
    sang = []
    fires = []
    answer = 0
    isVisited = [[0 for _ in range(C)] for _ in range(R)]
    fireVisited = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        world.append(list(input()))
        for j in range(C):
            if world[i][j] == '@':
                sangx, sangy = i, j
                sang.append([i, j])
                isVisited[i][j] = 1
            if world[i][j] == '*':
                fires.append([i, j])
                fireVisited[i][j] = 1

    if sangx == 0 or sangx == R-1 or sangy == 0 or sangy == C-1:
        print(1)
        continue

    while True:
        answer += 1
        nextFire = deque(fires.copy())
        checker = False
        fires = []
        while nextFire:
            fx, fy = nextFire.popleft()
            fireVisited[fx][fy] = 1
            for dx, dy in dir:
                nx, ny = dx+fx, dy+fy
                if 0<= nx < R and 0<= ny < C and fireVisited[nx][ny] == 0 and world[nx][ny] != '#':
                    fires.append([nx, ny])
                    fireVisited[nx][ny] = 1
                    world[nx][ny] = '*'

        nextSang = deque(sang.copy())
        sang = []

        while nextSang:
            x, y = nextSang.popleft()
            isVisited[x][y] = 1
            for dx, dy in dir:
                nx, ny = dx+x, dy+y
                if 0 <= nx < R and 0 <= ny < C and world[nx][ny] == '.' and isVisited[nx][ny] == 0:
                    if nx == 0 or nx == R-1 or ny == 0 or ny == C-1:
                        checker = True
                        print(answer + 1)
                        break
                    sang.append([nx, ny])
                    isVisited[nx][ny] = 1

            if checker:
                break
        if checker:
            break

        if len(sang) == 0:
            print("IMPOSSIBLE")
            break

