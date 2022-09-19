import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

isVisited = []
M, N, K = 0, 0, 0
arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(row, col):
    isVisited[row][col] = 1
    for i in range(4):
        tempx = col + dx[i]
        tempy = row + dy[i]
        if 0 <= tempx < M and 0 <= tempy < N and isVisited[tempy][tempx] != 1 and arr[tempy][tempx] == 1:
            dfs(tempy, tempx)

for i in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    isVisited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    for j in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    for k in range(N):
        for l in range(M):
            if isVisited[k][l] != 1 and arr[k][l] == 1:
                isVisited[k][l] = 1
                dfs(k, l)
                answer += 1
    print(answer)
