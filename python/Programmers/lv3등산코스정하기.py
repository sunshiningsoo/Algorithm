from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    # 여러 봉우리 등산 ㄴ
    # 여러 출입구 ㄴ
    world = defaultdict(list)
    for i in paths:
        world[i[0]].append([i[2], i[1]])
        world[i[1]].append([i[2], i[0]])

    summits.sort() # 나중에 순서대로 처리해서 같은 값이면 작은 값으로 업데이트 해주기 위해서
    check = set(summits)
    distance = [1e9] * (n+1)

    q = []
    
    # 다 같이 넣어줌으로써 결국 intensity를 찾으면 되는 거니까
    for gate in gates:
        heapq.heappush(q, [0, gate])
        distance[gate] = 0
    
    while q:
        intensity, now = heapq.heappop(q)
        if now in check or intensity > distance[now]:
            continue

        for weight, target in world[now]:
            new_intensity = max(weight, intensity)
            if new_intensity < distance[target]:
                distance[target] = new_intensity
                heapq.heappush(q, [new_intensity, target])

    answer = [0, 1e9]

    for i in summits:
        if distance[i] < answer[1]:
            answer[0] = i
            answer[1] = distance[i]

    return answer



### 시간초과 풀이
# def solution(n, paths, gates, summits):
#     # 여러 봉우리 등산 ㄴ
#     # 여러 출입구 ㄴ
#     answer = []
#     world = [[0 for _ in range(n+1)] for _ in range(n+1)]
#     isVisited = [0]* (n+1) # gate 번호 그대로 가져가면 됨
    
#     for i in paths:
#         world[i[0]][i[1]] = i[2]
#         world[i[1]][i[0]] = i[2]
    
#     def DFS(currentGate, maxInten):
#         if currentGate in summits:
#             answer.append([currentGate, maxInten])
#             return
#         isVisited[currentGate] = 1
#         for nextGateNum, weight in enumerate(world[currentGate]):
#             if weight != 0:
#                 if isVisited[nextGateNum] == 0 and nextGateNum not in gates:
#                     DFS(nextGateNum, max(weight, maxInten))
#                     isVisited[nextGateNum] = 0
                    
#     for i in gates:
#         isVisited = [0] * (n+1)
#         DFS(i, 0)
    
#     answer.sort(key=lambda x: x[0])
#     answer.sort(key=lambda x: x[1])
    
#     return answer[0]
