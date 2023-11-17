import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v+1)]
distance = [1000000]*(v+1)

for _ in range(e):
    startk, end, w = map(int, input().split())
    graph[startk].append([w, end])



def djikstra():
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        weight, now = heapq.heappop(heap)

        if distance[now] < weight:
            continue

        for i in graph[now]:
            if distance[i[1]] > weight + i[0]:
                distance[i[1]] = weight + i[0]
                heapq.heappush(heap, (weight + i[0], i[1]))

djikstra()

for i in range(1, len(distance)):
    if distance[i] == 1000000:
        print("INF")
    else:
        print(distance[i])

