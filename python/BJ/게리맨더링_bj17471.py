from collections import defaultdict

N = int(input())
graph = defaultdict(list)

peoples = list(map(int, input().split()))
peoples.insert(0, 0)
isVisited = [0 for _ in range(N + 1)]
for i in range(1, N+1):
    graph[i] = list(map(int, input().split()))[1:]


peopleSum = sum(peoples)
answer = 1e9

# N이 1 ~ 10
# 인구수 1 ~ 1000
#
# 1. 1개 ~ N//2 + 1개까지 나눠주고
# 2. 나눠준게 서로 연결되어 있는지 확인하고
#     맞다면
#     2-1. 인구수의 차이를 프린트
#     아니면
#     2-2. return 해서 다른 조합으로 체크
# 3. 나눌 방법이 없다면, -1 return




def peopleDifference(tempPlace):
    hap = 0
    for i in tempPlace:
        hap += peoples[i]

    return abs(peopleSum - hap*2)

def newbfs(arr):
    isVisited = [0 for _ in range(N + 1)]
    q = [arr[0]]
    while q:
        start = q.pop(0)
        isVisited[start] = 1
        for next in graph[start]:
            if next in arr and isVisited[next] == 0:
                q.append(next)
                isVisited[next] = 1
    for idx, value in enumerate(isVisited):
        if idx in arr and value == 0:
            return False

    return True


def realChecker(arr):
    global isVisited

    if newbfs(arr):
        return True
    else:
        return False



def relateChecker(tempcur):
    othercur = [i for i in range(1, N+1)]
    for i in range(len(tempcur)):
        tempcur[i] += 1
        othercur.remove(tempcur[i])

    # tempcur과 othrecur이 각각 서로 연결되어 있는 놈인지 체크
    if realChecker(tempcur) and realChecker(othercur):
        return True
    return False


def combi(idx, cur, targetnum):
    global answer
    if len(cur) == targetnum:
        if relateChecker(cur):
            answer = min(answer, peopleDifference(cur))
        return

    for i in range(idx+1, N):
        combi(i, cur + [i], targetnum)


for i in range(1, N//2+1): # N까지 다 볼 필요는 없고, 중간까지만 체크하면, other에서 체크해줌
    for j in range(N):
        combi(j, [j], i)

if answer == 1e9:
    print(-1)
else:
    print(answer)