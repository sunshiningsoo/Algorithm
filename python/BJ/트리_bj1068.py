from collections import defaultdict
N = int(input())
nodes = list(map(int, input().split()))
graph = defaultdict(list)
header = 0
for idx, node in enumerate(nodes):
    if node == -1:
        header = idx
        continue
    else:
        graph[node].append(idx)

deleteNode = int(input())

# 1. 선택한 노드에서 단방향으로 dfs해서 노드들 삭제해줌
# 2. 다음에 root에서 dfs돌면서 leaf 노드 확인해줌
isVisited = [0 for _ in range(N)]
answer = 0
def dfs(cur):
    global answer
    if cur == deleteNode:
        return
    cnt = 0
    for next_node in graph[cur]:
        if next_node == deleteNode:
            continue
        cnt += 1
        dfs(next_node)
    if cnt == 0 and cur != deleteNode:
        answer += 1

dfs(header)
print(answer)


