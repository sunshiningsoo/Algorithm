N = int(input())
M = int(input())
arr = [[0 for i in range(N)] for k in range(N)]
isVisited = [0] * N

for i in range(M):
    j, k = map(int, input().split())
    arr[j-1][k-1] = 1
    arr[k-1][j-1] = 1

def dfs(num):
    isVisited[num] = 1
    for i in range(len(arr[num])):
        if isVisited[i] != 1 and arr[num][i] == 1:
            dfs(i)

dfs(0)
print(sum(isVisited) - 1)