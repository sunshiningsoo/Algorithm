N = int(input())


for i in range(N):
    sum = 1
    div = 1
    count = 1
    arr = list(map(int, input().split()))
    for j in range(arr[1]-arr[0]+1, arr[1]+1):
        sum *= j
        div *= count
        count += 1
    print(sum // div)