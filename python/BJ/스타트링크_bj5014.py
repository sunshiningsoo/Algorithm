from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
isVisitedSet = set()
answer = 1e9

def dfs(cur, cnt):
    global answer
    if cur in isVisitedSet:
        return

    isVisitedSet.add(cur)
    if cur == G:
        answer = min(answer, cnt)
        return

    if cur < G:
        dfs(cur + U, cnt + 1)
    elif cur > G:
        dfs(cur - D, cnt + 1)

buildings = [0] * (F+1)

def dfs2(cur, cnt):
    global buildings
    buildings[cur] = cnt

    if cur == G:
        print(cnt)
        return
    # buildings[cur] = cnt
    if cur + U <= G and buildings[cur+U] == 0 and cur + U != S:
        dfs2(cur+U, cnt+1)
    if cur - D > 0 and buildings[cur-D] == 0 and cur - D != S:
        dfs2(cur-D, cnt+1)


def bfs():
    q = deque()
    q.append(S)
    while q:
        cur = q.popleft()
        if cur == G:
            print(buildings[cur])
            break

        if cur + U <= F and buildings[cur + U] == 0 and cur+U != S:
            buildings[cur+U] = buildings[cur] + 1
            q.append(cur + U)
        if cur - D > 0 and buildings[cur - D] == 0 and cur-D != S:
            buildings[cur - D] = buildings[cur] + 1
            q.append(cur - D)
    if buildings[G] == 0 and S != G:
        print("use the stairs")


# 메모리 초과
# dfs2(S, 0)
# if buildings[G] == 0 and S != G:
#     print("use the stairs")

bfs()

# if answer == 1e9:
#     print("use the stairs")
# else:
#     print(answer)
