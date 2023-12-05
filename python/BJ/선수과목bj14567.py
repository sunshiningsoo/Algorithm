from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

answerNode = [0] * (N+1)
indegreeZeroSet = set()

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegreeZeroSet.add(e)
    answerNode[e] += 1

tempAnswer = 0
isVisited = [0] * (N+1)
q = deque()
count = 1
answer = [0] * (N+1)
# TODO: indegree가 0 인놈을 순서대로 큐에 넣어서 제거해줌
for i in range(1, N+1):
    if i not in indegreeZeroSet:
        q.append([i, count])
        answer[i] = count

while q:
    target, targetCount = q.popleft()
    answer[target] = targetCount

    for node in graph[target]:
        answerNode[node] -= 1
        if answerNode[node] == 0:
            q.append([node, targetCount+1])


print(*answer[1:])


# 방향 반대로 바꾸어 depth 구하는 방식 -> 결과는 다르게 나옴
# def dfs(cur, count):
#     global tempAnswer
#     if answerNode[cur] != 0:
#         # print(f"cur: {cur}, {answerNode[cur]}")
#         tempAnswer = answerNode[cur] + 1
#         return
#     tempAnswer = max(tempAnswer, count)
#     isVisited[cur] = 1
#     for next_node in graph[cur]:
#         if isVisited[next_node] == 0:
#             dfs(next_node, count+1)
#
#
# for node in range(1, N+1):
#     tempAnswer = 0
#     isVisited = [0] * (N + 1)
#     dfs(node, 1)
#     answerNode[node] = tempAnswer
#
# print(*answerNode[1:])


