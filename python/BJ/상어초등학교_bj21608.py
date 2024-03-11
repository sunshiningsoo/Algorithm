N = int(input())
sunseo = []
favorites = {}
for i in range(N**2):
    posi = list(map(int, input().split()))
    sunseo.append(posi[0])
    favorites[posi[0]] = posi[1:]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def in_range(x, y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

world = [[0 for _ in range(N)] for _ in range(N)]

'''
1. 빈칸 중 좋아하는 학생이 인접한, 가장 많은 칸
2. 1여러개면, 인접한 칸 중 비어있는 칸이 많은 칸
3. 2도 여러개면, r 작고, c 작은 칸으로
'''

def first_check(num):
    maxnum = 0
    maxPoints = []
    for i in range(N):
        for j in range(N):
            if world[i][j] != 0:
                continue
            value = 0
            for dx, dy in dirs:
                nx = dx + i
                ny = dy + j
                if in_range(nx, ny) and world[nx][ny] in favorites[num]:
                    value += 1

            if value > maxnum:
                maxnum = value
                maxPoints = [[i, j]]
            elif value == maxnum:
                maxPoints.append([i, j])
    return maxPoints

def second_check(arrs):
    maxnum = 0
    maxPoints = []
    for x, y in arrs:
        value = 0
        for dx, dy in dirs:
            nx = x+dx
            ny = y+dy
            if in_range(nx, ny) and world[nx][ny] == 0:
                value += 1
        if value > maxnum:
            maxnum = value
            maxPoints = [[x, y]]
        elif value == maxnum:
            maxPoints.append([x, y])
    return maxPoints

def third_check(arrs):
    R, C = N+1, N+1
    for x, y in arrs:
        if x < R:
            R = x
            C = y
        elif x == R:
            if y < C:
                C = y
    return R, C

for person in sunseo:
    points = first_check(person)
    if len(points) > 1:
        second_points = second_check(points)
        if len(second_points) > 1:
            realX, realY = third_check(second_points)
            world[realX][realY] = person
        else:
            world[second_points[0][0]][second_points[0][1]] = person
    else:
        world[points[0][0]][points[0][1]] = person

answer = 0
dics = {0:0, 1:1, 2:10, 3:100, 4:1000}

for i in range(N):
    for j in range(N):
        temp = 0
        for dx, dy in dirs:
            nx = dx+i
            ny = dy + j
            if in_range(nx, ny) and world[nx][ny] in favorites[world[i][j]]:
                temp += 1

        answer += dics[temp]
# for i in world:
#     print(*i)
print(answer)



