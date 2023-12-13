from collections import defaultdict

n = int(input())

a, b = map(int, input().split())

q = int(input())
graph = defaultdict(list)
isVisited = [0] * (n+1)
for i in range(q):
    l, r = map(int, input().split())
    graph[l].append(r)
    graph[r].append(l)

q = [[a, 0]]
isVisited[a] = 1
chon = [0] * (n+1)
while q:
    cur, weight = q.pop(0)
    isVisited[cur] = 1
    if cur == b:
        break

    for i in graph[cur]:
        if isVisited[i] != 1:
            isVisited[i] = 1
            q.append([i, weight+1])
            chon[i] = weight+1

if chon[b] == 0:
    print(-1)
else:
    print(chon[b])


