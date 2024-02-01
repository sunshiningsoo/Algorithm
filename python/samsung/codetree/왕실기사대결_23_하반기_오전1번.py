# 1. 기사들과 그 초기 영향력 위치를 dictionary를 활용해 저장함
# 13시 40분에 시작 -> 15:45 종료
import copy

L, N, Q = map(int, input().split())
world = [] # 0 빈칸, 1 함정, 2 벽
crasher = []
for i in range(L):
    world.append(list(map(int, input().split())))
    for j in range(L):
        if world[i][j] == 1:
            crasher.append([i, j])

gisas = {}
gisaSparse = {}
originHealth = []
for i in range(1, N+1):
    # r, c, h, w, k
    gisas[i] = list(map(int, input().split()))
    gisas[i][0] -= 1
    gisas[i][1] -= 1
    temp = []
    originHealth.append(gisas[i][-1])
    for j in range(gisas[i][0], gisas[i][0]+gisas[i][2]):
        for k in range(gisas[i][1], gisas[i][1]+gisas[i][3]):
            temp.append([j, k])
    gisaSparse[i] = temp


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위 오 아 왼
death_gisa = set()

def in_range(x, y):
    if 0<=x<L and 0<=y<L and world[x][y] != 2:
        return True
    return False

def next_sparseCheck(gisa, direction, sparse):
    gisa_next_sparse = []
    for x, y in sparse[gisa]:
        nx, ny = x + dir[direction][0], y + dir[direction][1]
        if not in_range(nx, ny):
            gisa_next_sparse = []
            break
        gisa_next_sparse.append([nx, ny])
    return gisa_next_sparse

def crash_gisa_check(gisa, gisa_next_sparse, sparse):
    crash_gisa = []
    for key, value in sparse.items():
        if key == gisa:  # 나랑 안겹치는 기사 체크
            continue
        if value == []:
            continue
        if key in death_gisa: # 이거 체크로 통과 되고 안되고의 차이가 생김
            continue

        other_checker = False
        for other_gisa in value:
            if other_gisa in gisa_next_sparse:
                other_checker = True
                break
        if other_checker:
            crash_gisa.append(key)

    return crash_gisa

def healthChecker(gisaNum, tempgisaSparse, moveGisa):
    global gisaSparse
    global gisas
    # print(tempgisaSparse)
    for idx, value in tempgisaSparse.items():
        if idx == gisaNum:
            continue
        if idx in death_gisa:
            continue
        if idx not in moveGisa:
            continue

        temp = 0
        for crash in crasher:
            if crash in value:
                temp += 1
        gisas[idx][4] -= temp
        if gisas[idx][4] <= 0:
            death_gisa.add(idx)
            gisaSparse[idx] = []


def move(gisa, direction, crash_gisa):
    global gisaSparse

    cur = copy.deepcopy(crash_gisa)
    tempGisaSparse = copy.deepcopy(gisaSparse)
    moveGisa = set()
    moveGisa.add(gisa)

    cantMove = False
    while cur:
        next_gisa = cur.pop(0)
        moveGisa.add(next_gisa)
        next_gisa_sparse = next_sparseCheck(next_gisa, direction, tempGisaSparse)
        if len(next_gisa_sparse) == 0:
            cantMove = True
            break

        next_crashed = crash_gisa_check(next_gisa, next_gisa_sparse, tempGisaSparse)
        if len(next_crashed) == 0:
            tempGisaSparse[next_gisa] = next_gisa_sparse
        else:
            tempGisaSparse[next_gisa] = next_gisa_sparse
            cur += next_crashed

    if cantMove:
        return
    else:
        tempGisaSparse[gisa] = next_sparseCheck(gisa, direction, gisaSparse)
        healthChecker(gisa, tempGisaSparse, moveGisa)
        gisaSparse = tempGisaSparse


def king_direction(gisa, direction):
    # 기사가 죽은 기사라면 return
    if gisa in death_gisa:
        return

    gisa_next_sparse = next_sparseCheck(gisa, direction, gisaSparse)
    # 벽이나 경계 넘어간다면 이동 못함
    if len(gisa_next_sparse) == 0:
        return

    # 다른 기사와 걸리는 것 체크
    crash_gisa = crash_gisa_check(gisa, gisa_next_sparse, gisaSparse)
    if len(crash_gisa) == 0:
        # crash 안되니까 이동시키고
        gisaSparse[gisa] = gisa_next_sparse
        return
    else:
        # 걸리는 기사를 끝까지 밀 수 있나 체크, 만약 안된다면, return
        move(gisa, direction, crash_gisa)


for i in range(Q):
    a, d = map(int, input().split())
    king_direction(a, d)


temp = 0
for idx, value in gisas.items():
    if idx not in death_gisa:
        temp += originHealth[idx-1] - gisas[idx][-1]

print(temp)
