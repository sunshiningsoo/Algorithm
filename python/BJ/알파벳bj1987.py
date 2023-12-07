import sys
input = sys.stdin.readline

R, C = map(int, input().split())

world = []
for i in range(R):
    world.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
alphachecker = set()
alphachecker.add(ord(world[0][0]))

def dfs(x, y, curArr):
    global answer
    answer = max(answer, curArr)

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < R and 0 <= yy < C:
            if ord(world[xx][yy]) not in alphachecker:
                alphachecker.add(ord(world[xx][yy]))
                dfs(xx, yy, curArr+1)
                alphachecker.remove(ord(world[xx][yy]))


dfs(0, 0, 1)

print(answer)
