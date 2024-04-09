'''
N*N 격자
검은색: -1, 무지개: 0, 빈칸: -2

일반: M가지 색상(M 이하의 자연수로 표현됨)

인접한 칸: 상하좌우

블록 그룹:
 - 일반 블록 적어도 하나 있어야 함
 - 일반 블록의 색은 모두 같아야 함
 - 검은색 안되고, 무지개는 얼마든지 가능
 - 그룹에 속한 블록의 수는 2 이상
 - 기준블록이란 : 일반 블록 중 행 작고, 열 작은 것이 기준임


오토 플레이
 - 크기가 가장 큰 블록 그룹을 찾음,
    여러개라면 무지개 블록 수 가장 많은 블록
    기준 행이 가장 큰 것
    기준 열이 가장 큰 것

 - 1 그룹의 모든 블록 제거, B^2 점수 획득
 - 격자에 중력 (검은색 제외 모든 블록이 내려감)
 - 90도 반시계 회전
 - 격자에 중력

종료 조건
 - 블록 그룹이 없으면 끝
'''

N, M = map(int, input().split())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
totalAnswer = 0

def in_range(x, y):
    if 0<=x<N and 0<=y<N: return True
    return False

def gravity():
    global world
    realTemp = [[-2 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        temp = []
        for j in range(N):
            if world[N-1-j][i] == -1:
                temp.append([N-1-j, -1])
            elif world[N-1-j][i] >= 0:
                temp.append([-1, world[N-1-j][i]])

        ptr = 0
        # print(temp)
        for k in temp:
            if k[1] == -1:
                realTemp[k[0]][i] = -1
                ptr = N - k[0]
            else:
                realTemp[N-1-ptr][i] = k[1]
                ptr += 1

    for i in range(N):
        for j in range(N):
            world[i][j] = realTemp[i][j]


def rotate():
    global world
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[N-1-j][i] = world[i][j]

    for i in range(N):
        for j in range(N):
            world[i][j] = temp[i][j]


isVisited = [[0 for _ in range(N)] for _ in range(N)]

def canMove(target, x, y):
    global isVisited
    if in_range(x, y) and isVisited[x][y] == 0:
        if world[x][y] == target or world[x][y] == 0:
            return True
    return False

def find_bfs(target, x, y):
    global isVisited
    isVisited[x][y] = 1
    q = [[x, y]]
    gizunx, gizuny = x, y
    cnt = 0 #  그룹이 몇개인지
    rainbowCnt = 0
    rainbowGrid = []

    while q:
        cx, cy = q.pop(0)
        cnt += 1
        for dx, dy in dirs:
            nx = cx+dx
            ny = cy+dy
            if canMove(target, nx, ny):
                isVisited[nx][ny] = 1
                q.append([nx, ny])

                if world[nx][ny] == 0:
                    rainbowCnt += 1
                    rainbowGrid.append([nx, ny])
                elif world[nx][ny] != 0:
                    if nx <= gizunx:
                        gizunx = nx
                        if ny < gizuny:
                            gizuny = ny

    for xx, yy in rainbowGrid:
        isVisited[xx][yy] = 0

    if cnt >= 2:
        return [cnt, rainbowCnt, gizunx, gizuny]
    return []


def delete(x, y):
    global isVisited, world, totalAnswer
    isVisited = [[0 for _ in range(N)] for _ in range(N)]
    q = [[x, y]]
    isVisited[x][y] = 1
    target = world[x][y]
    world[x][y] = -2
    cnt = 0
    while q:
        cx, cy = q.pop(0)
        cnt += 1
        for dx, dy in dirs:
            nx = cx+dx
            ny = cy+dy
            if canMove(target, nx, ny):
                isVisited[nx][ny] = 1
                world[nx][ny] = -2
                q.append([nx, ny])

    totalAnswer += cnt**2

def print_world():
    global world
    for i in world:
        print(*i)
    print()

def find_group_block():
    global isVisited
    isVisited = [[0 for _ in range(N)] for _ in range(N)]

    cur_group = []
    for i in range(N):
        for j in range(N):
            if world[i][j] > 0 and isVisited[i][j] == 0:
                a = find_bfs(world[i][j], i, j)
                if a != []:
                    cur_group.append(a)

    if len(cur_group) == 0: return []

    cur_group.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
    cur = cur_group[0]
    delete(cur[2], cur[3])

    gravity()
    rotate()
    gravity()


while True:
    find_group = find_group_block()
    if find_group == []: break


print(totalAnswer)

