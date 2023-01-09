# https://www.acmicpc.net/problem/1051

N, M = map(int, input().split())
arr = []
ans = []

for i in range(N):
    arr.append(list(map(int, input())))

for row in range(N):
    for col in range(M):
        target = arr[row][col]
        for i in range(col, M):
            if target == arr[row][i] and row + i - col < N:
                if arr[row + i - col][col] == arr[row+i-col][i] == target:
                    ans.append(i - col + 1)

print(max(ans)**2)
