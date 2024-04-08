'''
1 ~ 2N-1
1: 올리는 위치
N: 내리는 위치

로봇은 올리는 위치에만 올릴 수 있음
내리는 위치에 도달하면, 그 즉시 내림

로봇은 스스로 이동 가능, 올리는 위치에 올리거나 이동하면
그 칸의 내구도는 즉시 1 감소

가장 먼저 올라간 로봇부터,
회전 방향으로 이동할 수 있으면 이동
    이동하려는 칸에 로봇이 없소, 내구도가 1이상 남아 있어야 함
없으면 가만히,

내구도가 0인 칸의 개수가 K개 이상이라면 종료

'''
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
world = deque([])
tt = list(map(int, input().split()))
for i in tt:
    world.append(i)

def countZeroPow():
    temp = 0
    for i in world:
        if i <= 0:
            temp += 1
    return temp

step = 0
robots = deque([0]*2*N)
# robots = [0]*(2*N)
robotNum = 1
while True:
    if countZeroPow() >= K:
        break

    # 1. 로봇과 함께 한칸 회전
    cur = world.pop()
    world.appendleft(cur)
    # world = [cur] + world
    rot = robots.pop()
    robots.appendleft(rot)
    # robots = [rot] + robots
    if robots[N-1] != 0: # 로봇 도달하면 바로 내려버림
        robots[N-1] = 0

    # 2. 내리는 위치 도달하면 즉시 내려야 함
    mapping = []
    for idx, tempRobot in enumerate(robots):
        if tempRobot > 0:
            mapping.append([tempRobot, idx])

    mapping.sort(key=lambda x: x[0])
    # print()
    # print(mapping)
    # print(world)
    # print(robots)
    for r, i in mapping:
        targetIdx = i+1
        if world[targetIdx] >=1 and robots[targetIdx] == 0:
            robots[i] = 0
            robots[targetIdx] = r
            world[targetIdx] -= 1
            if targetIdx == N-1:
                robots[targetIdx] = 0

    # 3. 올리는 위치 내구도가 0이 아니면, 올리는 위치에 로봇을 올림
    if world[0] > 0 and robots[0] == 0:
        world[0] -= 1
        robots[0] = robotNum
        robotNum += 1

    step += 1

print(step)





