N = int(input())

arr =[[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    temp = []
    for k in map(int, input().split()):
        temp.append(k)
    for j in range(len(temp)):
        arr[i][j] = temp[j]

for i in range(1, N):
    for k in range(N):
        if k == 0:
            arr[i][k] = arr[i-1][k] + arr[i][k]
        else:
            arr[i][k] = max(arr[i-1][k], arr[i-1][k-1]) + arr[i][k]

print(max(arr[N-1]))
