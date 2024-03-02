from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = defaultdict(list)
costs = [1e9]* (N+1)
for i in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

realStart, realEnd = map(int, input().split())
q = []
heapq.heappush(q, [0, realStart])
costs[realStart] = 0
while q:
    cur_w, cur_node = heapq.heappop(q)

    if cur_w > costs[cur_node]:
        continue

    for next_w, next_node in graph[cur_node]:
        new_w = cur_w + next_w
        if new_w < costs[next_node]:
            heapq.heappush(q, [new_w, next_node])
            costs[next_node] = new_w

print(costs[realEnd])
