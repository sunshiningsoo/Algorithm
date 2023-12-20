import sys

input = sys.stdin.readline

row, col = map(int, input().split())

world = []
virusPlace = []
oneCount = 0
for i in range(row):
    world.append(list(map(int, input().split())))
    for j in range(len(world[i])):
        if world[i][j] == 2:
            virusPlace.append([i, j])

        if world[i][j] == 1:
            oneCount += 1
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
isVisited = [[0 for _ in range(len(world[0]))] for _ in range(len(world))]


def checkVirus(currentWorld):

    q = virusPlace.copy()
    virusVisited = [[0 for _ in range(len(world[0]))] for _ in range(len(world))]

    hap = 0
    while q:
        x, y = q.pop(0)
        virusVisited[x][y] = 1
        hap += 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<len(world) and 0<=yy<len(world[0]):
                if currentWorld[xx][yy] == 0 and virusVisited[xx][yy] != 1:
                    virusVisited[xx][yy] = 1
                    q.append([xx, yy])

    return row*col - hap - oneCount - 3


def wall(currentWorld, checker, x, y):
    global answer
    if checker == 3:
        answer = max(answer, checkVirus(currentWorld))
        return

    for i in range(x, len(world)):
        for j in range(len(world[0])):
            if currentWorld[i][j] == 0 and isVisited[i][j] != 1:
                currentWorld[i][j] = 1
                isVisited[i][j] = 1
                wall(currentWorld, checker+1, i, j)
                isVisited[i][j] = 0
                currentWorld[i][j] = 0

wall(world, 0, 0, 0)
print(answer)
