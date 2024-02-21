# 13:10
# N*N, M턴
# 루돌프 움직 -> 1번 ~ P번 산타 움직 (기절 or 탈락 산타는 안 움직)
# 거리는 좌표 제곱
#
# 루돌프, 우선순위: 거리 가장 가까운 산타에게 돌진, r 크고, c 크고
# 8방향으로 우선순위 높은 산타에게 가까워지는 방향으로 돌진
#
# 산타, 루돌프에게 가장 가까워지는 방향으로 이동
# 다른 산타가 있거나 밖으로는 못 움직임
# 움직일 수 있는 칸이 없으면 안움직임 + 있어도 가까워질 수 있는 방법이 없으면 안움직
# 거리, 상우하좌 우선순위
#
# 충돌: 루돌프가 충돌 -> 산타가 C만큼의 점수 + 루돌프의 방향으로 C칸 밀려남
# 산타가 충돌 -> 산타 D점 + 산타가 이동한 반대 방향으로 D칸 밀려남
#
# 밀려난 곳이 밖이면 탈락, 산타가 있으면 상호작용
#
# 상호작용: 산타가 착지하는 칸에서만 상호작용, 연쇄적 밀려남
#
# 기절: 산타는 충돌 후 기절, k번째 턴이었다면, k+1 턴까지 기절, k+2 턴부터 정상

N, M, P, C, D = map(int, input().split())
world = [[0 for _ in range(N)] for _ in range(N)]

rudolx, rudoly = map(int, input().split())
rudolx -= 1
rudoly -= 1
deathSanta = set()

rudoldx = [-1, -1, -1, 0, 0, 1, 1, 1]
rudoldy = [-1, 0, 1, -1, 1, -1, 0, 1]
santadx = [-1, 0, 1, 0]
santady = [0, 1, 0, -1]
gizulSanta = [1e9 for _ in range(P+1)]
answer = [0 for _ in range(P+1)]
turn = 1
for i in range(P):
    santa, santax, santay = map(int, input().split())
    santax -= 1
    santay -= 1
    world[santax][santay] = santa

def distance(r1, r2, c1, c2):
    return (r1-r2)**2 + (c1-c2)**2

def in_range(x, y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

# world에 남아있는 산타 스캔
def remainSantaScan():
    remain = []
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] != 0:
                # 번호, r, c 순
                remain.append([world[i][j], i, j])
    return remain

def crash(targetSanta, isRudolCrash):
    # nx, ny, distance i
    global rudolx, rudoly, turn
    nx, ny, dis, i = targetSanta

    if isRudolCrash:
        currentSanta = world[nx][ny]
        if currentSanta not in deathSanta:
            answer[currentSanta] += C
            world[nx][ny] = 0
            nnx = nx + rudoldx[i]*C
            nny = ny + rudoldy[i]*C
            gizulSanta[currentSanta] = turn
            if not in_range(nnx, nny):
                deathSanta.add(currentSanta)
                return

            q = [[currentSanta, nnx, nny]]

            while q:
                curNum, x, y = q.pop(0)
                if not in_range(x, y):
                    deathSanta.add(curNum)
                    break
                if world[x][y] == 0:
                    world[x][y] = curNum
                    break
                else:
                    q.append([world[x][y], x+rudoldx[i], y+rudoldy[i]])
                    world[x][y] = curNum

    else:
        currentSanta = world[nx+santadx[(i+2)%4]][ny+santady[(i+2)%4]]
        if currentSanta not in deathSanta:
            answer[currentSanta] += D
            world[nx+santadx[(i+2)%4]][ny+santady[(i+2)%4]] = 0

            nnx = nx + santadx[(i+2)%4]*D
            nny = ny + santady[(i+2)%4]*D
            gizulSanta[currentSanta] = turn
            if not in_range(nnx, nny):
                deathSanta.add(currentSanta)
                return

            q = [[currentSanta, nnx, nny]]

            while q:
                curNum, x, y = q.pop(0)
                if not in_range(x, y):
                    deathSanta.add(curNum)
                    break
                if world[x][y] == 0:
                    world[x][y] = curNum
                    break
                else:
                    q.append([world[x][y], x+santadx[(i+2)%4], y+santady[(i+2)%4]])
                    world[x][y] = curNum


def rudolMove():
    global rudolx, rudoly
    remainSanta = remainSantaScan()
    if len(remainSanta) == 0:
        return
    for i in range(len(remainSanta)):
        remainSanta[i].append(distance(rudolx, remainSanta[i][1], rudoly, remainSanta[i][2]))

    remainSanta.sort(key=lambda x: (x[3], -x[1], -x[2]))
    targetSanta = remainSanta[0].copy()
    rudolSpace = []
    for i in range(8):
        nx = rudolx + rudoldx[i]
        ny = rudoly + rudoldy[i]
        if in_range(nx, ny):
            rudolSpace.append([nx, ny, distance(nx, targetSanta[1], ny, targetSanta[2]), i])

    rudolSpace.sort(key=lambda x: x[2])
    nextSanta = rudolSpace[0].copy()
    rudolx = nextSanta[0]
    rudoly = nextSanta[1]

    if [rudolx, rudoly] == [targetSanta[1], targetSanta[2]]:
        crash(nextSanta, True)


def santaMove():
    global rudolx, rudoly, turn

    remainSanta = remainSantaScan()
    remainSanta.sort(key=lambda x: x[0])

    for santaNum, x, y in remainSanta:
        # 산타가 움직이면서 나머지 산타들의 좌표가 바뀔 수 있음!!!!!!! -> 밀어내면 답없음
        if santaNum in deathSanta:
            continue
        for i in range(len(world)):
            for j in range(len(world[0])):
                if world[i][j] == santaNum:
                    x, y = i, j
        if gizulSanta[santaNum] == turn or gizulSanta[santaNum] == turn - 1:
            continue

        curDistance = distance(x, rudolx, y, rudoly)

        santaSpace = []
        for i in range(4):
            nx = x + santadx[i]
            ny = y + santady[i]
            if in_range(nx, ny) and world[nx][ny] == 0:
                santaSpace.append([nx, ny, distance(nx, rudolx, ny, rudoly), i])
        if len(santaSpace) == 0:
            continue
        santaSpace.sort(key=lambda x: (x[2], x[3]))

        if curDistance <= santaSpace[0][2]:
            continue

        nextSanta = santaSpace[0].copy()

        if [nextSanta[0], nextSanta[1]] == [rudolx, rudoly]:
            crash(nextSanta, False)
        else:
            world[x][y] = 0
            world[nextSanta[0]][nextSanta[1]] = santaNum
        if deathSantaCheck() or not worldSum():
            return

def deathSantaCheck():
    if len(list(deathSanta)) == P:
        return True
    return False

def worldSum():
    temp = 0
    for i in world:
        temp += sum(i)

    if temp == 0:
        return False
    return True


def game():
    rudolMove()
    if deathSantaCheck() or not worldSum():
        return
    santaMove()
    if deathSantaCheck() or not worldSum():
        return

for i in range(1, M+1):
    turn += 1
    game()
    if deathSantaCheck() or not worldSum():
        break

    for j in range(1, P+1):
        if j not in deathSanta:
            answer[j] += 1

print(*answer[1:])
