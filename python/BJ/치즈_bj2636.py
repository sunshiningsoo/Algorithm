from collections import deque
r, c = map(int, input().split())
world = []
cheeses = set()
for i in range(r):
    world.append(list(map(int, input().split())))
    for j in range(c):
        if world[i][j] == 1:
            cheeses.add((i, j))

round = 0

def resolver(arr): # arr = [[a, b]]
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr
    else:
        return [arr[0], arr[-1]]


def sumWorld():
    hap = 0
    for i in world:
        hap += sum(i)
    return hap

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    isVisitedSet = set()
    cheeseSet = set()
    round += 1
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        isVisitedSet.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and (nx, ny) not in isVisitedSet:
                if world[nx][ny] == 0:
                    isVisitedSet.add((nx, ny))
                    q.append((nx, ny))
                elif world[nx][ny] == 1:
                    cheeseSet.add((nx, ny))

    for x, y in cheeseSet:
        world[x][y] = 0

    if sumWorld() == 0:
        print(round)
        print(len(list(cheeseSet)))
        break




# 1트 상하좌우에서 총쏴서 첫번째, 마지막 값이 최외각이라 생각 -> 개같이 실패임
# while True:
#     roundCheese = set()
#     round += 1
#
#     # 가로
#     for i in range(r):
#         temp = []
#         for j in range(c):
#             if world[i][j] == 1:
#                 temp.append([i, j])
#
#         for j in resolver(temp):
#             roundCheese.add((j[0], j[1]))
#
#     for i in range(c):
#         temp = []
#         for j in range(r):
#             if world[j][i] == 1:
#                 temp.append([j, i])
#
#         for j in resolver(temp):
#             roundCheese.add((j[0], j[1]))
#
#     for x, y in roundCheese:
#         world[x][y] = 0
#
#     if sumWorld() == 0:
#         print(round)
#         print(roundCheese)
#         break
#
