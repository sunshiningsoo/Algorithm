import copy
R, C = map(int, input().split())

# 빨간 구슬을 구멍으로 빼내는 것, 파란 구슬이 들어가지 않도록!
# 동시에 둘다 빠질 수 있음, 10번 이하로 기울여서 뺼수 있냐?

redLoc = []
blueLoc = []
holeLoc = []
world = []
isVisited = [[[[0 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]

for i in range(R):
    world.append(list(input()))
    for j in range(C):
        if world[i][j] == 'R':
            redLoc = [i, j]
        if world[i][j] == 'B':
            blueLoc = [i, j]
        if world[i][j] == 'O':
            holeLoc = [i, j]

# 상하좌우
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

answer = False


def mover_enhance(direction, redL, blueL):
    countR = 0
    countB = 0
    tempR = copy.deepcopy(redL)
    tempB = copy.deepcopy(blueL)

    while world[tempR[0]+dx[direction]][tempR[1]+dy[direction]] != '#' and world[tempR[0]][tempR[1]] != 'O':
        tempR[0] += dx[direction]
        tempR[1] += dy[direction]
        countR += 1

    while world[tempB[0]+dx[direction]][tempB[1]+dy[direction]] != '#' and world[tempB[0]][tempB[1]] != 'O':
        tempB[0] += dx[direction]
        tempB[1] += dy[direction]
        countB += 1

    return tempR, tempB, countR, countB


def copy_graph(graph):
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            temp[i][j] = graph[i][j]
    return temp


def printWorld(graph):
    for i in graph:
        print(*i)


def check(dep, redL, blueL):
    global answer
    if dep > 10:
        return
    isVisited[redL[0]][redL[1]][blueL[0]][blueL[1]] = 1

    for i in range(4):
        redLL, blueLL, countR, countB = mover_enhance(i, redL, blueL)
        # print(blueLL)
        # printWorld(copygraph)
        if world[blueLL[0]][blueLL[1]] == 'O':
            continue

        if world[redLL[0]][redLL[1]] == 'O':
            answer = True
            return

        if redLL == blueLL:
            if countR > countB:
                redLL[0] -= dx[i]
                redLL[1] -= dy[i]
            elif countR < countB:
                blueLL[0] -= dx[i]
                blueLL[1] -= dy[i]

        if isVisited[redLL[0]][redLL[1]][blueLL[0]][blueLL[1]] == 0:
            check(dep + 1, redLL, blueLL)
            if answer:
                # print(redLL, blueLL)
                return
            isVisited[redLL[0]][redLL[1]][blueLL[0]][blueLL[1]] = 0


check(1, redLoc, blueLoc)
if answer:
    print(1)
else:
    print(0)









# 졌잘싸.. 일자에 같이 있는 경우에 체크해주기 힘듬
# def mover(direction, graph, redL, blueL):
#
#     redX = dx[direction] + redL[0]
#     redY = dy[direction] + redL[1]
#
#     while 0<= redX < R and 0<= redY < C:
#         if graph[redX][redY] == '#' or graph[redX][redY] == 'B':
#             break
#         if graph[redX][redY] == '.':
#             temp = graph[redL[0]][redL[1]]
#             graph[redL[0]][redL[1]] = graph[redX][redY]
#             graph[redX][redY] = temp
#
#         elif graph[redX][redY] == 'O':
#             graph[redL[0]][redL[1]] = '.'
#             break
#         elif graph[redX][redY] == '#':
#             break
#         redL = [redX, redY]
#         redX = dx[direction] + redL[0]
#         redY = dy[direction] + redL[1]
#
#     blueX = dx[direction] + blueL[0]
#     blueY = dx[direction] + blueL[1]
#
#     while 0<= blueX < R and 0<= blueY < C:
#         if graph[blueX][blueY] == '#' or graph[blueX][blueY] == R:
#             break
#         if graph[blueX][blueY] == '.':
#             temp = graph[blueL[0]][blueL[1]]
#             graph[blueL[0]][blueL[1]] = graph[blueX][blueY]
#             graph[blueX][blueY] = temp
#
#         elif graph[blueX][blueY] == 'O':
#             # 실패
#             graph[blueL[0]][blueL[1]] = 'WTF'
#             break
#         elif graph[blueX][blueY] == '#':
#             break
#         blueL = [blueX, blueY]
#         blueX = dx[direction] + blueL[0]
#         blueY = dy[direction] + blueL[1]
#
#     return graph, redL, blueL
#
