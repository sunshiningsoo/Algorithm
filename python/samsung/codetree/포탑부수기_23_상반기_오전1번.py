'''
N X M의 격자
총 K번이 반복됨

1. 공격자 선정
- 부서지지 않은 포탑 중 가장 약한 포탑이 공격자
- 몇개의 조건
- N+M만큼의 공격력이 증가됨

2. 공격자의 공격
- 자신을 제외한 가장 강한 포탑 공격
- 몇개의 조건

2-1. 레이저 공격
1. 상하좌우 이동가능, 부서진 포탑 못가고, 가장자리 이동 쌉가능
최단 경로로 공격하고, 경로 없다면 '포탄공격'으로 전환
최단 경로 여러개면, '우하좌상' 순서로
해당 수치만큼 공격력 줄고, 이동 경로의 포탑들은 절반 만큼 공격 받음

2-2. 포탄 공격
던져서 공격 + 8방향 영향받음 + 공격자는 피해 안봄

3. 0 되면 부서지고
4. 정비: 공격과 무관한 포탑은 공격력이 1씩 올라감

'''

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
isVisited = [[0 for _ in range(M)] for _ in range(N)]

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

attackHistory = {}
for i in range(N):
    for j in range(M):
        attackHistory[(i, j)] = 0

def pickAlivePotap():
    potaps = []
    for i in range(N):
        for j in range(M):
            if world[i][j] > 0:
               potaps.append([world[i][j], attackHistory[(i, j)], i+j, j, i])
    return potaps

def pickAnotherPotap(r, c):
    potaps = []
    for i in range(N):
        for j in range(M):
            if world[i][j] > 0 and [i, j] != [r, c]:
               potaps.append([world[i][j], attackHistory[(i, j)], i+j, j, i])
    return potaps

def potanThrow(attacker, target):
    global world
    # print("throw")
    eightDivisions = [(1, 0), (1, -1), (1, 1),
                      (-1, 0), (-1, -1), (-1, 1),
                      (0, 1), (0, -1)]
    # 힘, 히스토리, 좌표합, col, row
    affected = [[attacker[-1], attacker[-2]], [target[-1], target[-2]]]
    world[target[-1]][target[-2]] -= world[attacker[-1]][attacker[-2]]

    for dx, dy in eightDivisions:
        nx = (dx + target[-1]) # % N
        ny = (dy + target[-2]) # % M
        if nx == -1:
            nx = N - 1
        if nx == N:
            nx = 0
        if ny == -1:
            ny = M - 1
        if ny == M:
            ny = 0

        if world[nx][ny] > 0 and [nx, ny] != [attacker[-1], attacker[-2]]:
            world[nx][ny] -= world[attacker[-1]][attacker[-2]] // 2
            affected.append([nx, ny])

    return affected

# 우하좌상
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def razerAttack(attacker, target):
    global isVisited
    global world
    sx, sy = attacker[-1], attacker[-2]
    ex, ey = target[-1], target[-2]
    q = deque([])
    q.append([[sx, sy]])
    isVisited = [[0 for _ in range(M)] for _ in range(N)]
    isVisited[sx][sy] =1
    while q:

        arrs = q.popleft()
        if arrs[-1] == [ex, ey]:
            arrs = arrs[1:]
            if len(arrs) == 1:
                a, b = arrs[0]
                world[a][b] -= attacker[0]
            elif len(arrs) > 1:
                for ta, tb in arrs[:-1]:
                    world[ta][tb] -= attacker[0]//2
                a, b = arrs[-1]
                world[a][b] -= attacker[0]
            return [[sx, sy]] + arrs

        for dx, dy in dirs:
            nx = (arrs[-1][0] + dx)
            ny = (arrs[-1][1] + dy)
            if nx == -1:
                nx = N-1
            if nx == N:
                nx = 0
            if ny == -1:
                ny = M-1
            if ny == M:
                ny = 0
            if isVisited[nx][ny] == 0 and world[nx][ny] > 0:
                isVisited[nx][ny] = 1
                # print(arrs + [[nx, ny]])
                q.append(arrs + [[nx, ny]])

    return []


def attack(attacker, target):
    affected = razerAttack(attacker, target)
    if affected == []:
        affected = potanThrow(attacker, target)

    return affected

def reSetting(affectedXY):
    for i in range(N):
        for j in range(M):
            if world[i][j] <= 0:
                world[i][j] = 0
            if world[i][j] > 0 and [i, j] not in affectedXY:
                world[i][j] += 1


def pickAlivePotap1():
    pow = 100000
    ax, ay = 0, 0
    for i in range(N):
        for j in range(M):
            if world[i][j] <= 0:
                continue
            if world[i][j] < pow:
                pow = world[i][j]
                ax, ay = i, j
            elif world[i][j] == pow:
                if attackHistory[(i, j)] > attackHistory[(ax, ay)]:
                    ax, ay = i, j
                elif attackHistory[(i, j)] == attackHistory[(ax, ay)]:
                    if i+j > ax+ay:
                        ax, ay = i, j
                    elif i+j == ax+ay:
                        if j > ay:
                            ay = j
    return ax, ay

def pickAnotherPotap1(x, y):
    pow = -1
    ax, ay = 0, 0
    for i in range(N):
        for j in range(M):
            if world[i][j] <= 0: continue
            if [i, j] == [x, y]: continue
            if world[i][j] > pow:
                ax, ay = i, j
                pow = world[i][j]
            elif world[i][j] == pow:
                if attackHistory[(i, j)] < attackHistory[(ax, ay)]:
                    ax, ay = i, j
                elif attackHistory[(i, j)] == attackHistory[(ax, ay)]:
                    if i+j < ax+ay:
                        ax, ay = i, j
                    elif i+j == ax+ay:
                        if j < ay:
                            ax, ay = i, j

    return ax, ay

round = 1

def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if world[i][j] > 0:
                cnt += 1
    return cnt

while K:

    ## 1. 공격자 선택
    alives = pickAlivePotap()
    if len(alives) == 0:
        break
    attacker = None
    xx, yy = pickAlivePotap1()
    for i in alives:
        if [i[-1], i[-2]] == [xx, yy]:
            attacker = i
            break

    # 힘, 히스토리, 좌표합, col, row
    world[attacker[-1]][attacker[-2]] += N+M
    attacker[0] += N+M

    ## 2. 공격자의 공격
    anothers = pickAnotherPotap(attacker[-1], attacker[-2])
    if len(anothers) == 0:
        break

    xx, yy = pickAnotherPotap1(attacker[-1], attacker[-2])
    targetPotap = None
    for i in anothers:
        if [i[-1], i[-2]] == [xx, yy]:
            targetPotap = i
            break

    affectedXY = attack(attacker, targetPotap)
    reSetting(affectedXY)
    ## 4. 포탑 정비
    round += 1
    K -= 1
    if K == 0:
        break

    if check() < 2:
        break

    ## 5. last. setting
    attackHistory[(attacker[-1], attacker[-2])] = round

ans = 0
for i in world:
    ans = max(max(i), ans)

print(ans)
