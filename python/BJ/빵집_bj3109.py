import sys
input = sys.stdin.readline
r, c = map(int, input().split())

world = []
for i in range(r):
    world.append(list(input()))

dir = [(-1, 1), (0, 1), (1, 1)] # 우상, 우우, 우하

checkSet = set()
answer = 0

def mover(x, y):
    global answer
    if y == c-1:
        answer += 1
        return True

    for dx, dy in dir:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in checkSet and world[nx][ny] != 'x':
            checkSet.add((nx, ny))
            if mover(nx, ny):
                return True
    return False


def start():
    for i in range(r):
        if (i, 0) not in checkSet:
            checkSet.add(((i, 0)))
            mover(i, 0)

start()
print(answer)
