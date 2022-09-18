N, M, start = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
bool = [0 for _ in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1
    arr[j-1][i-1] = 1


def dfs(num):
    if bool[num] == 1:
        return
    bool[num] = 1
    print(num+1, end=' ')
    for i in range(N):
        if arr[num][i] == 1 and num != i:
            # bool[i] = 1
            # print(i+1, end=' ')
            dfs(i)

tempque = []
def bfs(num):
    tempque.append(num)
    bool[num] = 1
    while len(tempque):
        a = tempque[0]
        del tempque[0]
        print(a+1, end=' ')
        for i in range(N):
            if arr[a][i] == 1 and a != i and bool[i] != 1:
                tempque.append(i)
                bool[i] = 1

dfs(start-1)
bool = [0 for _ in range(N)]
print('')
bfs(start-1)