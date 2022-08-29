N, M = map(int, input().split())
arr = []

# 이건 내가 처음에 만든거
def backTracking(now):
    if now == M:
        for i in arr:
            print(i, end=' ')
        print("")
    else:
        isVisited = [0] * 10
        for i in range(1, N+1):
            if not isVisited[i]:
                arr.append(i)
                isVisited[i] = 1
                backTracking(now + 1)
                isVisited[i] = 0
                arr.pop()

# 사실은 더하고 빼기만 하면 되는 거였음 '.';;;
def backTracking2(now):
    if len(arr) == M:
        for i in arr:
            print(i, end=" ")
        print("")
    else:
        for i in range(1, N+1):
            arr.append(i)
            backTracking(now+1)
            arr.pop()



backTracking2(0)