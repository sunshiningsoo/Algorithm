import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = []

for i in range(E):
    start, end, weight = map(int, input().split())
    heapq.heappush(nodes, [weight, start, end])


answer = 0

nodesParent = [i for i in range(V+1)]

def getParent(a):
    if a == nodesParent[a]:
        return nodesParent[a]
    else:
        nodesParent[a] = getParent(nodesParent[a])
    return nodesParent[a]

def union(start, end):
    s = getParent(start)
    e = getParent(end)
    if s > e:
        nodesParent[start] = e
    else:
        nodesParent[end] = s

while nodes:
    weight, start, end = heapq.heappop(nodes)
    a = getParent(start)
    b = getParent(end)
    if a != b:
        union(a, b)
        answer += weight

    else:
        continue

print(answer)


