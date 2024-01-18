import sys
input = sys.stdin.readline

N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

answer = 0

# 1번 선수가 일단 4번으로 침
taja = 0

def inningHap(idx, cur_line_up):
    global taja
    out = 0
    j1, j2, j3 = 0, 0, 0
    tempInning = 0

    while out != 3:
        curTaja = cur_line_up[taja]
        if world[idx][curTaja] == 0:
            out += 1
        elif world[idx][curTaja] == 1:
            tempInning += j3
            j1, j2, j3 = 1, j1, j2
        elif world[idx][curTaja] == 2:
            tempInning += j2+j3
            j1, j2, j3 = 0, 1, j1
        elif world[idx][curTaja] == 3:
            tempInning += j1+j2+j3
            j1, j2, j3 = 0, 0, 1
        elif world[idx][curTaja] == 4:
            tempInning += j1 + j2 + j3 + 1
            j1, j2, j3 = 0, 0, 0

        taja = (taja + 1) % 9

    return tempInning


def game(line_up):
    global taja
    taja = 0
    tempHap = 0
    for i in range(N):
        tempHap += inningHap(i, line_up)

    return tempHap

isVisited = [0 for _ in range(9)]

def sunseo(cur):
    global answer
    if len(cur) == 9:
        if cur[3] != 0:
            return
        answer = max(answer, game(cur))
        return

    for i in range(9):
        if isVisited[i] == 1:
            continue
        if len(cur) > 4 and cur[3] != 0:
            return

        isVisited[i] = 1
        sunseo(cur + [i])
        isVisited[i] = 0

sunseo([])

print(answer)
