# https://www.acmicpc.net/problem/7562
N = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for i in range(N):
    width = int(input())
    startX, startY = map(int, input().split())
    targetX, targetY = map(int, input().split())
    isVisited = [[0 for _ in range(width)] for _ in range(width)]
    mapCount = 0
    answer = 1000000
    q = [[startX, startY, mapCount]]
    isVisited[startX][startY] = 1
    while q:
        temp = q.pop(0)
        currentx = temp[0]
        currenty = temp[1]
        value = temp[2]
        if currentx == targetX and currenty == targetY:
            answer = min(answer, value)
        for i in range(8):
            xx = currentx + dx[i]
            yy = currenty + dy[i]
            if 0<=xx<width and 0<=yy<width:
                if isVisited[xx][yy] == 0:
                    isVisited[xx][yy] = 1
                    q.append([xx, yy, value + 1])

    print(answer)
