import copy
import sys
input = sys.stdin.readline

r, c, d = map(int, input().split())
world = []
answer = 0

for _ in range(r):
    world.append(list(map(int, input().split())))

# 총 3명의 궁수
# 각 턴 마다 궁수들 동시에 공격
# 거리가 d 이하인 적 중에서 가장 가깝고, 가장 왼쪽
#
# 적은 궁수가 공격하고 나서 아래로 한칸 이동
# 제일 아래로 가면 제외
# 모든 적이 격자에서 제외되면 게임 끝

def distance(a, b):
    # print(a, b)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def scanEnemy(currentWorld):
    enemys = []
    for i in range(r):
        for j in range(c):
            if currentWorld[i][j] == 1:
                enemys.append([i, j])

    return enemys

def dropEnemy(beforeEnemy):
    afterEnemy = [[0 for _ in range(c)] for _ in range(r)]
    cnt = 0
    for i in range(r-1):
        for j in range(c):
            afterEnemy[i+1][j] = beforeEnemy[i][j]
            if beforeEnemy[i][j] == 1:
                cnt += 1

    return afterEnemy, cnt

def kill(enemy, gungsoos):
    killedEnemy = []
    for gungsoo in gungsoos:
        killtarget = []
        for idx, e in enumerate(enemy):
            dis = distance(gungsoo, e)
            killtarget.append([dis, e[0], e[1]])
        killtarget.sort(key=lambda x: (x[0], x[2]))
        # print(killtarget)
        if killtarget[0][0] <= d:
            killedEnemy.append((killtarget[0][1], killtarget[0][2]))
    # print(killedEnemy)
    return killedEnemy


def checker(gungsoo):
    tempAnswer = 0
    for i in range(3):
        gungsoo[i] = [r, gungsoo[i]]
    # print(gungsoo)
    tempWorld = copy.deepcopy(world)

    while True:
        enemy = scanEnemy(tempWorld)
        killed = kill(enemy, gungsoo)
        tempAnswer += len(list(set(killed)))
        for i, j in killed:
            tempWorld[i][j] = 0

        tempWorld, cnt = dropEnemy(tempWorld)
        if cnt == 0:
            break
    return tempAnswer


def pickThree(idx, cur):
    global answer
    if len(cur) == 3:
        returnedValue = checker(cur)
        answer = max(answer, returnedValue)
        return

    for i in range(idx+1, c):
        pickThree(i, cur + [i])


for i in range(c-2):
    pickThree(i, [i])





print(answer)







