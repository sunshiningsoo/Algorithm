import copy
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

# TODO: 1. 상어가 먹을 것이 없으면 종료
# TODO: 2. 나보다 작은 먹을 것이 있다면 가서 먹음
# TODO: 3. 먹을 것이 많은데 그 거리가 동일하다면, 1.상단 2.왼쪾부터 먹음
# TODO: 4. 몸집만큼 먹어야 상어몸집 자람

# TODO: 1 상어 몸집보다 작은 놈이 있는지 확인, 없다면 종료
# TODO: 2 있다면, 거리 가장 가까운 녀석(몸집 큰놈이 중간에 있다면 쳐주지 말아야 함 BFS?)이 누군지 찾고,
# TODO: 3 거리 가장 가까운 녀석이 여러개라면 ~ 에 대한 처리
# TODO: 4 먹이 먹고, 상어몸집 +1, 상어 이동

target = defaultdict(list)
sharkM = 2
sharkR = 0
sharkC = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

for i in range(N):
    for j in range(N):
        if world[i][j] == 9:
            sharkR = i
            sharkC = j
            continue
        if world[i][j] != 0:
            target[world[i][j]].append([i, j])


def shortestPath(targets):
    temptargets = copy.deepcopy(targets)
    # temptargets = targets.copy()
    for idx, tempTarget in enumerate(temptargets):
        # tempTarget = [1, 4] 와 같은 작은 타겟임

        q = deque()
        isVisited = [[0 for _ in range(N)] for _ in range(N)]

        q.append([sharkR, sharkC, 0])
        isVisited[sharkR][sharkC] = 1
        checked = False
        while q:
            if checked:
                break
            r, c, cnt = q.popleft()
            isVisited[r][c] = 1
            for i in range(4):
                rr = r + dx[i]
                cc = c + dy[i]
                if 0 <= rr < N and 0 <= cc < N and isVisited[rr][cc] != 1 and world[rr][cc] <= sharkM:
                    isVisited[rr][cc] = 1
                    q.append([rr, cc, cnt + 1])
                    if [rr, cc] == tempTarget:
                        temptargets[idx].append(cnt + 1)
                        checked = True
                        break
    returntemp = []
    for i in temptargets: # 해당 먹이까지 못가는 경우가 존재하기 때문임
        if len(i) != 2:
            returntemp.append(i)
    return returntemp


sharkCurrentEat = 0

while True:
    tempTarget = []
    for i in range(1, sharkM):
        for j in target[i]:
            tempTarget.append(j)

    if len(tempTarget) == 0:
        break
    path = shortestPath(tempTarget)
    if len(path) == 0:
        break
    # print(path)
    path.sort(key=lambda x: [x[2], x[0], x[1]])


    targetr, targetc, targetCnt = path[0]
    answer += targetCnt

    if [targetr, targetc] in target[world[targetr][targetc]]:
        target[world[targetr][targetc]].remove([targetr, targetc])

    world[targetr][targetc] = 0
    world[sharkR][sharkC] = 0

    sharkR, sharkC = targetr, targetc
    sharkCurrentEat += 1
    if sharkCurrentEat == sharkM:
        sharkM += 1
        sharkCurrentEat = 0

print(answer)
