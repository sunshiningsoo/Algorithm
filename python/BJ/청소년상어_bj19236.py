'''
번호 1 ~ 16
방향 8방향

상어 (0, 0) 에 먼저 들어가서 먹음

물고기 이동:
1. 번호가 작은 물고기부터
이동 가능칸: 빈칸, 다른 물고기가 있는 칸
이동 불가능: 상어가 있거나, 공간의 경계 넘는 칸

이동할 수 있는 칸을 향할때까지 반시계 45도 회전
이동할 수 있는 칸 없으면, 이동 안함
다른 물고기 위치로 가면 서로의 위치를 바꿈

상어 여러 칸 이동 가능, 물고기 먹고, 물고기의 방향을 가짐
이동중의 물고기는 안먹음
물고기 없는 칸으로는 이동 불가

이동 가능한 칸 없으면 집감

상어가 먹을 수 있는 물고기 번호의 합의 최댓값!

'''

# 방향: 0 ~ 7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
world = []
fishes = {}
deathFish = []
for _ in range(4):
    arr = list(map(int, input().split()))
    tempworld = []
    for i in range(0, len(arr), 2):
        fishes[arr[i]] = arr[i+1]-1
        tempworld.append(arr[i])
    world.append(tempworld)

realWorld = {}
for i in range(len(world)):
    for j in range(len(world)):
        realWorld[(i, j)] = world[i][j]


ans = 0

def in_range(x, y):
    if 0<=x<4 and 0<=y<4: return True
    return False

def fishmove(sx, sy):
    global deathFish, fishes
    for idx in range(1, 17):
        if idx in deathFish: continue
        curx, cury = 0, 0
        # TODO: 시뮬레이션을 이동시킬때, 순서대로 이동시키면, 앞의놈을 이동시키다 뒤의 값이 변경될 수 있기때문에
        # TODO: Constant 한 값으로 계속 가기보다, 변경된 값을 확인하고 가져가는 과정이 필요하다.
        for i, value in realWorld.items():
            if value == idx:
                curx, cury = i[0], i[1]
                break
        # 가능한 곳 찾기, 이동, 상어가 있거나 밖이면 못감
        for i in range(fishes[idx], fishes[idx]+len(dx)):
            nx = curx + dx[i%len(dx)]
            ny = cury + dy[i%len(dx)]
            if not in_range(nx, ny): continue
            if [nx, ny] == [sx, sy]: continue

            realWorld[(nx, ny)], realWorld[(curx, cury)] = realWorld[(curx, cury)], realWorld[(nx, ny)]
            fishes[realWorld[(nx, ny)]] = i%len(dx)
            break


def solution(tempAns, sharkx, sharky, sharkdir):
    global ans, realWorld, deathFish, fishes
    if tempAns > ans:
        ans = tempAns
    before = {}
    beforeDic = {}
    for idx, value in fishes.items():
        beforeDic[idx] = value
    for idx, value in realWorld.items():
        before[idx] = value

    # TODO: 물고기 움직이기
    fishmove(sharkx, sharky)

    # TODO: 상어 움직이기
    for i in range(1, 4):
        nx = sharkx + dx[sharkdir]*i
        ny = sharky + dy[sharkdir]*i
        if in_range(nx, ny):
            if realWorld[(nx, ny)] in deathFish: continue

            temp = realWorld[(nx, ny)]
            deathFish.append(temp)
            solution(tempAns+temp, nx, ny, fishes[temp])
            deathFish.remove(temp)
            # TODO: 여기서 이전 값을 써주면 왜 안되지?
            # 이 상황에서 이전 Step으로 돌아가는 것이 아니라, 현재 상황에서 다음 칸만 확인하는 것이기 때문에
            # 전체 맵을 바꿀 필요는 없다.
            # fishes = beforeDic
            # realWorld = before
        else:
            break
    fishes = beforeDic
    realWorld = before


deathFish.append(realWorld[(0, 0)])
sharkdirs = fishes[realWorld[(0, 0)]]

solution(realWorld[(0, 0)], 0, 0, sharkdirs)


print(ans)

