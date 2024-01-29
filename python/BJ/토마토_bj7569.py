from collections import deque
import sys

input = sys.stdin.readline

c, r, h = map(int, input().split())

tong = [[] for _ in range(h)]
tomatos = []
tomatoCount = 0
minusCount = 0

for i in range(h):
    for j in range(r):
        tong[i].append(list(map(int, input().split())))
        for k in range(c):
            if tong[i][j][k] == 1:
                tomatoCount += 1
                tomatos.append([i, j, k]) # h, r, c
            if tong[i][j][k] == -1:
                minusCount += 1

dir = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
q = deque(tomatos)
visitSet = set()
answer = 0
if len(q) == 0:
    print(-1)
    exit()

def tomatoEndCheck():
    check = 0
    check += len(list(visitSet))

    if check == h*r*c - minusCount:
        return True
    else:
        return False

if not tomatoEndCheck():
    nq = deque([])

    while True:
        popH, popR, popC = q.popleft()
        visitSet.add((popH, popR, popC))

        for dh, dr, dc in dir:
            nh = dh + popH
            nr = dr + popR
            nc = dc + popC
            if 0<=nh<h and 0<=nr<r and 0<=nc<c:
                if (nh, nr, nc) not in visitSet and tong[nh][nr][nc] == 0:
                    visitSet.add((nh, nr, nc))
                    nq.append([nh, nr, nc])

        if len(q) == 0:
            if len(nq) != 0:
                q = nq.copy()
                nq = deque([])
                answer += 1
            elif len(nq) == 0:
                break

if tomatoEndCheck():
    print(answer)
else:
    print(-1)


