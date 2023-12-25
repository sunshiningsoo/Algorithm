N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
spreadX = [[-2, -1, -1, -1, 0, 1, 1, 1, 2],
           [0, 1, 0, -1, 2, 1, 0, -1, 0],
           [2, 1, 1, 1, 0, -1, -1, -1, -2],
           [0, -1, 0, 1, -2, -1, 0, 1, 0]
           ]
spreadY = [[0, -1, 0, 1, -2, -1, 0, 1, 0],
           [-2, -1, -1, -1, 0, 1, 1, 1, 2],
           [0, 1, 0, -1, 2, 1, 0, -1, 0],
           [2, 1, 1, 1, 0, -1, -1, -1, -2]
           ]
percentage = [2, 10, 7, 1, 5, 10, 7, 1, 2]


step = 1
curx, cury = N // 2, N // 2
direction = 0
tempcnt = 0
answer = 0
while [curx, cury] != [0, 0]:
    if tempcnt == step:
        direction = (direction + 1) % 4
    if tempcnt == 2 * step:
        step += 1
        tempcnt = 0
        direction = (direction + 1) % 4

    xx = curx + dx[direction]
    yy = cury + dy[direction]
    if 0<=xx<N and 0<=yy<N:
        targetAmount = world[xx][yy]
        tempHap = 0
        for i in range(len(spreadX[0])):
            targetX = xx + spreadX[direction][i]
            targetY = yy + spreadY[direction][i]

            if 0<=targetX<N and 0<=targetY<N:
                world[targetX][targetY] += (targetAmount*percentage[i]) // 100
            else:
                answer += (targetAmount*percentage[i]) // 100

            tempHap += (targetAmount * percentage[i]) // 100

        targetX = xx + dx[direction]
        targetY = yy + dy[direction]
        if 0 <= targetX < N and 0 <= targetY < N:
            world[targetX][targetY] += (targetAmount - tempHap)
        else:
            answer += (targetAmount - tempHap)

        world[xx][yy] = 0
        curx = xx
        cury = yy

    tempcnt += 1

print(answer)
