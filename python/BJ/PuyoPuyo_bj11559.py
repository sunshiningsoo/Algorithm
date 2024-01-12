from collections import deque
world = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(12):
    world.append(list(input()))
answer = 0

# bfs로 체크하고, 내려버리기 시전
isVisited = [[0 for _ in range(6)] for _ in range(12)]


def printWorld():
    for i in world:
        print(*i)
    print()

def clearVisited():
    global isVisited
    isVisited = [[0 for _ in range(6)] for _ in range(12)]

puyo = []
def bfsChecker(x, y):
    global answer
    global puyo
    q = deque()
    q.append([x, y, world[x][y]])
    isVisited[x][y] = 1
    temppuyo = []
    while q:
        curx, cury, target = q.popleft()
        temppuyo.append([curx, cury])
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and world[nx][ny] == target and isVisited[nx][ny] == 0:
                q.append([nx, ny, target])
                isVisited[nx][ny] = 1

    if len(temppuyo) >= 4:
        puyo += temppuyo


def gravity():
    global world
    for i in range(6):
        stack = []
        for j in range(12):
            if world[11 - j][i] != '.':
                stack.append(world[11-j][i])
                world[11 - j][i] = '.'
        for idx, value in enumerate(stack):
            world[11-idx][i] = value


while True:
    for i in range(12):
        for j in range(6):
            if world[i][j] != '.' and isVisited[i][j] == 0:
                bfsChecker(i, j)

    if len(puyo) >= 4:
        for x, y in puyo:
            world[x][y] = '.'
        clearVisited()
        gravity()
        # printWorld()
        answer += 1
        puyo = []
    else:
        break


print(answer)
