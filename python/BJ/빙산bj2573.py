import sys
input = sys.stdin.readline

row, col = map(int, input().split())

world = []
for i in range(row):
    world.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def minusFunc(minusValue):
    for i in range(row):
        for j in range(col):
            world[i][j] -= minusValue[i][j]
            if world[i][j] < 0:
                world[i][j] = 0

def melting(x, y, checked):
    minusValue = [[0 for _ in range(col)] for _ in range(row)]
    q = [[x, y]]

    while q:
        xx, yy = q.pop(0)
        checked[xx][yy] = 1
        temp = 0
        for i in range(4):
            dxx = xx + dx[i]
            dyy = yy + dy[i]
            if 0 <= dxx < row and 0 <= dyy < col and world[dxx][dyy] != 0 and checked[dxx][dyy] != 1:
                checked[dxx][dyy] = 1
                q.append([dxx, dyy])
            if 0 <= dxx < row and 0 <= dyy < col and world[dxx][dyy] == 0:
                temp += 1

        minusValue[xx][yy] = temp

    minusFunc(minusValue)

count = 0
splitIsland = 0
while True:
    splitIsland = 0
    checked = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if world[i][j] != 0 and checked[i][j] != 1:
                melting(i, j, checked)
                splitIsland += 1

    if splitIsland > 1:
        break

    hap = 0
    for i in world:
        hap += sum(i)
    if hap == 0:
        break
    count += 1

if splitIsland == 1:
    print(0)
else:
    print(count)

