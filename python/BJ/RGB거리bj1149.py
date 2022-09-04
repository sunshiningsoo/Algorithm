N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for k in range(1, N):
    # for 문을 계속해서 중첩해 풀려고 하면, 헷갈리고, 시간초과가 될 수있기에, 이렇게 풀어주는 방법
    arr[k][0] = min(arr[k-1][1], arr[k-1][2]) + arr[k][0]
    arr[k][1] = min(arr[k-1][0], arr[k-1][2]) + arr[k][1]
    arr[k][2] = min(arr[k-1][0], arr[k-1][1]) + arr[k][2]

print(min(arr[N-1]))
