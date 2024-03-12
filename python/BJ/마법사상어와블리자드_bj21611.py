"""
1. 마법 시전
    d, s 로 던져 구슬 파괴
2. 앞으로 댕겨지기, 폭발
    4개 이상 연속 -> 폭발 -> 2반복
3. 변하기
    갯수, 종류 2개로 변환됨 -> 칸보다 많아지면, 버림
4. 답
    1*1번 구슬 터짐 + 2*2번 구슬 터짐 + 3*3번 구슬 터짐
"""

N, M = map(int, input().split())
world = []
sharkR, sharkC = N // 2, N // 2
magicDir = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

roomMover = [(0, -1), (1, 0), (0, 1), (-1, 0)]
answerDic = {1:0, 2:0, 3:0}
for i in range(N):
    world.append(list(map(int, input().split())))

def magic():
    d, s = map(int, input().split())
    for i in range(1, s+1):
        world[sharkR+i*magicDir[d][0]][sharkC+i*magicDir[d][1]] = 0

def printAnswer():
    answer = 0
    for key, value in answerDic.items():
        if key != 0:
            answer += key*value
    print(answer)
def in_range(x, y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

def toOneDimension():
    roomDir = 3
    curx, cury = sharkR, sharkC
    temp = []
    isVisited = [[0 for _ in range(N)] for _ in range(N)]
    isVisited[sharkR][sharkC] = 1
    while True:
        if [curx, cury] == [0, 0]:
            break
        roomDir = (roomDir+1)%4

        nx = curx + roomMover[roomDir][0]
        ny = cury + roomMover[roomDir][1]
        if in_range(nx, ny):
            if isVisited[nx][ny] == 0:
                temp.append(world[nx][ny])
                isVisited[nx][ny] = 1
                curx = nx
                cury = ny
            elif isVisited[nx][ny] == 1:
                roomDir -= 1
                if roomDir == -1:
                    roomDir = 3

                nx = curx + roomMover[roomDir][0]
                ny = cury + roomMover[roomDir][1]
                temp.append(world[nx][ny])
                isVisited[nx][ny] = 1
                curx = nx
                cury = ny

    return temp

def deleteZeroRecur(arrs):
    tempArr = arrs.copy()
    while True:
        newArr = []
        zeroCnt = 0
        for i in tempArr:
            if i != 0:
                newArr.append(i)
            elif i == 0:
                zeroCnt += 1

        if zeroCnt == 0:
            break

        if not newArr:
            break


        ptr = 1
        curValue = newArr[0]
        cnt = 1
        # 4개 이상으로 있는거 찾고 0으로
        while ptr < len(newArr):
            thisValue = newArr[ptr]
            if curValue != thisValue:
                if cnt >= 4:
                    for i in range(ptr-cnt, ptr):
                        newArr[i] = 0
                    answerDic[curValue] += cnt

                curValue = thisValue
                cnt = 1

            elif curValue == thisValue:
                cnt += 1

            ptr += 1
        if cnt >= 4:
            if newArr[ptr-cnt] != 0:
                answerDic[newArr[ptr-cnt]] += ptr
            for i in range(ptr-cnt, ptr):
                newArr[i] = 0

        tempArr = newArr.copy()
    if not newArr:
        return []
    return tempArr

def change(arrs):
    curValue = arrs[0]
    ptr = 1
    curCnt = 1
    temp = []
    while ptr < len(arrs):
        thisValue = arrs[ptr]
        if thisValue != curValue:
            temp.append(curCnt)
            temp.append(curValue)
            curValue = thisValue
            curCnt = 1
        else:
            curCnt += 1

        ptr += 1

    temp.append(curCnt)
    temp.append(curValue)

    return temp

def batch(now):
    global world
    if len(now) > N*N -1 :
        now = now[:N*N-1]

    world = [[0 for _ in range(N)] for _ in range(N)]
    roomDir = 3
    isVisited = [[0 for _ in range(N)] for _ in range(N)]
    isVisited[sharkR][sharkC] = 1
    curx, cury = sharkR, sharkC
    ptr = 0
    while True:
        if [curx, cury] == [0, 0]:
            break

        roomDir = (roomDir+1) % 4
        nx = curx + roomMover[roomDir][0]
        ny = cury + roomMover[roomDir][1]
        if in_range(nx, ny):
            if isVisited[nx][ny] == 0:
                world[nx][ny] = now[ptr]
                curx, cury = nx, ny
                isVisited[nx][ny] = 1
            elif isVisited[nx][ny] == 1:
                roomDir -= 1
                if roomDir == -1:
                    roomDir = 3
                nx = curx + roomMover[roomDir][0]
                ny = cury + roomMover[roomDir][1]
                world[nx][ny] = now[ptr]
                isVisited[nx][ny] = 1
                curx = nx
                cury = ny
        ptr += 1
        if ptr == len(now):
            break


for i in range(M):
    # 1. 마법시전 -> 1차원 arr로 다루자
    magic()
    oneDimension = toOneDimension()
    deleteArr = deleteZeroRecur(oneDimension)
    if not deleteArr:
        break
    now = change(deleteArr)
    batch(now)


printAnswer()