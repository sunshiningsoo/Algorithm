import sys
input = sys.stdin.readline
C, R, H = map(int, input().split())

world = [[0 for _ in range(C)] for _ in range(H)]
answer = 4

for i in range(R):
    a, b = map(int, input().split())
    world[a-1][b-1] = 1

def checker(tempworld):
    idxs = [i for i in range(C)]
    for i in range(H):
        arr = []
        for j in range(C):
            if tempworld[i][j] == 1:
                arr.append(j)
        for idx in arr:
            idxs[idx], idxs[idx+1] = idxs[idx+1], idxs[idx]
    if idxs == [i for i in range(C)]:
        return True
    return False


def boundCheck(x, y, nowWorld):
    if y == 0 and nowWorld[x][y+1] == 0:
        return True
    if y > 0 and nowWorld[x][y-1] == 0 and nowWorld[x][y+1] == 0:
        return True

    return False


def backTrack(nx, ny, cnt, nowWorld):
    global answer
    if cnt >= answer or cnt > 3:
        return
    if checker(nowWorld):
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    now = 0
    for i in range(nx, H):
        if i == nx:
            now = ny
        else:
            now = 0
        for j in range(now, C-1):
            if nowWorld[i][j] == 0 and boundCheck(i, j, nowWorld):
                nowWorld[i][j] = 1
                backTrack(i, j+2, cnt+1, nowWorld)
                nowWorld[i][j] = 0

backTrack(0, 0, 0, world)

if answer > 3:
    print(-1)
else:
    print(answer)

# 4 3 4
# 1 1
# 2 2
# 1 3