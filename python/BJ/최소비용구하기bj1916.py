import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]
distance = [1e9] * (N+1) # 이거 그냥 두면, cost의 최소비용이라서 edge 업데이트 안됨, -> 그래서 무한대 값으로 설정

for i in range(M):
    u, v, cost = map(int, input().split())
    bus[u].append([cost, v])
start, end = map(int, input().split())
k = []
def solution():
    
    heapq.heappush(k, (0, start))
    distance[start] = 0

    while k:
        currentCost, currentNode = heapq.heappop(k)
        
        if distance[currentNode] < currentCost:
            continue
        
        for edge in bus[currentNode]:
            newCost = currentCost + edge[0]
            if distance[edge[1]] > newCost:
                distance[edge[1]] = newCost
                heapq.heappush(k, (newCost, edge[1]))

solution()
print(distance[end])

