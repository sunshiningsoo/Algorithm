N = int(input())

appleNum = int(input())

# 맵 인덱스는 1보다 커야하고, appleNum까지임
world = [[0 for _ in range(N+1)] for _ in range(N + 1)]

for i in range(appleNum):
    x, y = map(int, input().split())
    world[x][y] = 'a'

direction = int(input())
dirs = []

for i in range(direction):
    dirs.append(list(map(str, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

wormdir = 1 # 오른쪽
wormPlace = [1, 1]
timer = 0
crash = False
world[1][1] = 1

wormQ = [[1, 1]]
def printWorld():
    for i in world:
        print(*i)
    print()

for i in range(len(dirs)):
    turnTime, turnDir = int(dirs[i][0]), dirs[i][1]
    if i > 0:
        turnTime -= int(dirs[i-1][0])

    while turnTime:
        if wormPlace[0]+dx[wormdir] < 1 or \
            wormPlace[0] + dx[wormdir] > N or \
            wormPlace[1] + dy[wormdir] < 1 or \
             wormPlace[1] + dy[wormdir] > N:
            # print("CRASH")
            crash = True
            break
        if world[wormPlace[0]+dx[wormdir]][wormPlace[1]+dy[wormdir]] == 1:
            # print("CRASH")
            crash = True
            break


        if world[wormPlace[0] + dx[wormdir]][wormPlace[1] + dy[wormdir]] != 'a':
            a, b = wormQ.pop(0)
            world[a][b] = 0

        wormQ.append([wormPlace[0] + dx[wormdir], wormPlace[1] + dy[wormdir]])

        world[wormPlace[0] + dx[wormdir]][wormPlace[1] + dy[wormdir]] = 1

        wormPlace[0] += dx[wormdir]
        wormPlace[1] += dy[wormdir]
        # printWorld()
        turnTime -= 1
        timer += 1

    if turnDir == 'D':
        wormdir = (wormdir+1) % 4
    elif turnDir == 'L':
        wormdir -= 1
        if wormdir < 0:
            wormdir = 3

    if crash:
        break

if 1<=wormPlace[0]<N and 1<=wormPlace[1]<N and not crash:
    while True:
        if wormPlace[0]+dx[wormdir] < 1 or \
            wormPlace[0] + dx[wormdir] > N or \
            wormPlace[1] + dy[wormdir] < 1 or \
             wormPlace[1] + dy[wormdir] > N:
            # print("CRASH")
            crash = True
            break
        if world[wormPlace[0]+dx[wormdir]][wormPlace[1]+dy[wormdir]] == 1:
            # print("CRASH")
            crash = True
            break


        if world[wormPlace[0] + dx[wormdir]][wormPlace[1] + dy[wormdir]] != 'a':
            a, b = wormQ.pop(0)
            world[a][b] = 0

        wormQ.append([wormPlace[0] + dx[wormdir], wormPlace[1] + dy[wormdir]])

        world[wormPlace[0] + dx[wormdir]][wormPlace[1] + dy[wormdir]] = 1

        wormPlace[0] += dx[wormdir]
        wormPlace[1] += dy[wormdir]
        # printWorld()
        timer += 1



print(timer+1)
