import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]


for i in range(M):
    l, r, w = map(int, input().split())
    graph[l].append([w, r])
    graph[r].append([w, l])


v1, v2 = map(int, input().split())


def djikstra(graph, start):
    q = []
    distance = [1e9] * (N + 1)
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        current_weight, current_node = heapq.heappop(q)

        if current_weight > distance[current_node]:
            continue

        for next_weight, next_node in graph[current_node]:
            new_distance = next_weight + current_weight
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(q, [new_distance, next_node])

    return distance


new_distance1 = djikstra(graph, 1)
new_distance2 = djikstra(graph, v1)
new_distance3 = djikstra(graph, v2)

answer = min(new_distance1[v1]+new_distance2[v2]+new_distance3[N], new_distance1[v2]+new_distance3[v1]+new_distance2[N])
if answer >= 1e9:
    print(-1)
else:
    print(answer)




# 1 -> N v1, v2
# 1 -> v1, v2, -> N
# 1 -> v2, v1 -> N