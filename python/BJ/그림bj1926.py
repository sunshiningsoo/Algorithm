row, col = map(int, input().split())

world =[]
for i in range(row):
    world.append(list(map(int, input().split())))

isVisited = [[0 for _ in range(col)] for _ in range(row)]

printCount = 0
maxPrint = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(r, c):
    q = [[r, c]]
    temp = 0
    while q:
        x, y = q.pop(0)
        temp += 1
        isVisited[x][y] = 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<row and 0<=yy<col:
                if isVisited[xx][yy] != 1 and world[xx][yy] == 1:
                    isVisited[xx][yy] = 1
                    q.append([xx, yy])

    return temp


for i in range(row):
    for j in range(col):
        if isVisited[i][j] == 0 and world[i][j] == 1:
            maxPrint = max(maxPrint, solution(i, j))
            printCount += 1

print(printCount)
print(maxPrint)

