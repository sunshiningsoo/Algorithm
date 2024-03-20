from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, root, q = map(int, input().split())
graph = defaultdict(list)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = [0] * (N+1)
def dfs(cur):
    cnt[cur] = 1
    for nx in graph[cur]:
        if cnt[nx] == 0:
            dfs(nx)
            cnt[cur] += cnt[nx]

dfs(root)

for q in range(q):
    print(cnt[int(input())])


'''
하위의 방법은 edge들을 다 끊어버리는 것이었는데, 시간초과임
'''
# setter = [root]
# checker = set()
# while setter:
#     temp = set()
#     for idx, value in graph.items():
#         for target in setter:
#             if target in graph[idx] and idx not in checker:
#                 graph[idx].remove(target)
#                 checker.add(target)
#                 temp.add(idx)
#
#     setter = list(temp)
#
#
# def bfs(node):
#     isVisited = [0] * (N+1)
#     isVisited[node] = 1
#     q = deque()
#     q.append(node)
#     cnt = 0
#     while q:
#         cur = q.popleft()
#         cnt += 1
#         for nx in graph[cur]:
#             if isVisited[nx] == 0:
#                 isVisited[nx] = 1
#                 q.append(nx)
#     print(cnt)
#
# for i in query:
#     bfs(i)




