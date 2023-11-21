import heapq
from collections import defaultdict

graph = defaultdict(list)

random = [[1, 2, 3], [2, 3, 5], [1, 3, 4]]

for i in random:
    graph[i[0]].append([i[2], i[1]])
    graph[i[1]].append([i[2], i[0]])

distance = [1e9] * (len(graph.keys()) + 1)

def djikstra(startingPoint):
    q = []
    heapq.heappush(q, [0, startingPoint])
    distance[1] = 0

    while q:
        currentWeight, current = heapq.heappop(q)

        for next_weight, next_node in graph[current]:
            # 없어도 노상관인데 탐색 시간을 줄이는데 큰 공을 세움
            if distance[next_node] < currentWeight: # 기존의 값보다 큰 값이라면 체크해줄 필요도 없음
                continue

            # 새로 추가되는 노드의 weight + 추가되는 노드로부터 추가되지 않은 노드들의 최솟값 업데이트
            new_distance = currentWeight + next_weight
            if distance[next_node] > new_distance:
                distance[next_node] = new_distance
                heapq.heappush(q, [new_distance, next_node])


djikstra(1)
print(distance)




