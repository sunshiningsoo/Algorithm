# https://www.acmicpc.net/problem/2178
N, M = map(int, input().split())
world = []
for _ in range(N):
    world.append(list(input()))

isVisited = [[0 for _ in range(M)] for _ in range(N)]
isVisited[0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(row, col):
    q = [(row, col)]
    while q:
        tempPop = q.pop(0)
        for i in range(4):
            x = tempPop[1] + dx[i]
            y = tempPop[0] + dy[i]
            if 0 <= x < M and 0 <= y < N:
                if isVisited[y][x] == 0 and world[y][x] == '1':
                    isVisited[y][x] = isVisited[tempPop[0]][tempPop[1]] + 1
                    q.append((y, x))

# DFS의 경우에 깊이우선 탐색이니까, 최소거리 예외케이스가 존재할 가능성이 있음
def DFS(row, col):
    for i in range(4):
        x = col + dx[i]
        y = row + dy[i]
        if 0 <= x < M and 0 <= y < N:
            if isVisited[y][x] == 0 and world[y][x] == '1':
                isVisited[y][x] = isVisited[row][col] + 1
                DFS(y, x)


BFS(0, 0)

print(isVisited[N-1][M-1])
