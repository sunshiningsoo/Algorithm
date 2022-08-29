N, M = map(int, input().split())
arr = []

def backTracking(now):
    if len(arr) == M:
        for i in arr:
            print(i, end=" ")
        print("")
    else:
        for i in range(now, N+1):
            if i not in arr:
                arr.append(i)
                backTracking(i+1)
                arr.pop()

backTracking(1)
