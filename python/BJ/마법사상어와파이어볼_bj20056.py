import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, K = map(int, input().split())
# fireball = []
world = defaultdict(list)
new_dic = defaultdict(list)
for i in range(M):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    # r c m s d
    world[(temp[0], temp[1])].append(temp[2:])

# 방향으로 스피드 칸 만큼 움직이는 거임
# 칸을 넘어간다면 반대쪽 칸으로 들어옴, d: 방향, s: 속력

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 하나씩 다 돌리고, 칸 2개 이상인 얘들 처리해주면 될듯?
# 한번 다 돌리면 다시 큐에 넣어주고,

def exceptionHandle(tempWorld):
    # 4개로 나눠지는 경우
    totalM = 0
    totalS = 0
    oddIndexChecker = 0
    evenIndexChecker = 0
    cnt = len(tempWorld)
    for i in tempWorld:
        totalM += i[0]
        totalS += i[1]
        if i[2] % 2 == 0:
            evenIndexChecker += 1
        else:
            oddIndexChecker += 1
    if totalM // 5 == 0:
        return []
    newIdx = []
    if evenIndexChecker == cnt or oddIndexChecker == cnt:
        newIdx = [0, 2, 4, 6]
    else:
        newIdx = [1, 3, 5, 7]

    returnValue = []

    for i in range(4):
        # if totalM // 5 < 0:
        #     return []  여기 이 조건이 있을 때 시간초과가 안나는 이유가 뭐지...?
        returnValue.append([totalM//5, totalS//cnt, newIdx[i]])

    return returnValue


def fireballChecker():
    for key in new_dic.keys():
        if len(new_dic[key]) > 1:
            world[key] = exceptionHandle(new_dic[key])
        else:
            world[key].append(new_dic[key][0])
    new_dic.clear()


def move():
    global fireball
    global world
    for key in world.keys():
        for m, s, d in world[key]:
            nr = (key[0] + dx[d]*s) % N
            nc = (key[1] + dy[d]*s) % N
            new_dic[(nr, nc)].append([m, s, d])
    world.clear()


for i in range(K):
    move()
    fireballChecker()

answer = 0
for i in world.keys():
    for j in list(world[i]):
        answer += j[0]

print(answer)
