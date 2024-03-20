N = int(input())
q = int(input())
dic = {}
for i in range(1, N+1):
    dic[i] = []

for i in range(q):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
isVisited = [0 for _ in range(N+1)]

q = [[1, 0]]
isVisited[1] = 1
ans = 0
while q:
    cur, cnt = q.pop(0)
    if cnt <= 2:
        ans += 1

    for nx in dic[cur]:
        if isVisited[nx] == 0 and cnt <= 2:
            isVisited[nx] = 1
            q.append([nx, cnt+1])

if ans != 0:
    print(ans-1)
else:
    print(0)