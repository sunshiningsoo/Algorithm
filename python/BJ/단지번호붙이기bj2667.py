# REF: https://www.acmicpc.net/problem/2667
N = int(input())
map = []
apa = []

for i in range(N):
    map.append(list(input()))

isVisited = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

def DFS(x, y):
    global count
    count += 1
    isVisited[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx < N and 0<= yy < N:
            if isVisited[xx][yy] != 1 and map[xx][yy] == '1':
                DFS(xx, yy)


for i in range(N):
    for j in range(N):
        if isVisited[i][j] == 0 and map[i][j] == '1':
            DFS(i, j)
            apa.append(count)
            count = 0

print(len(apa))
apa.sort()
for i in range(len(apa)):
    print(apa[i])
