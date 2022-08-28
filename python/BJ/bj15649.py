# 백트래킹

N, k = map(int, input().split())
isVisitedArr = [0 for _ in range(10)]
historyList = []

def backTracking(now):
    if now == k:
        for i in historyList:
            print(i, end= ' ')
        print("")
        return
    else:
        # nextNow = now + 1
        for i in range(1, N+1):
            if isVisitedArr[i] != 1:
                historyList.append(i)
                isVisitedArr[i] = 1
                backTracking(now + 1)
                isVisitedArr[i] = 0
                historyList.pop()

backTracking(0)