from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
nodeChecker = [0] * (V + 1)
graph = defaultdict(list)

for i in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

nodeNumbers = [0] * (V+1)
node_num = 1
cut = [0] * (V+1)

def dfs(currentNode, isRoot):
    global node_num
    node_num += 1
    nodeChecker[currentNode] = node_num
    ret = nodeChecker[currentNode]
    child = 0

    for nextNode in graph[currentNode]:
        if nodeChecker[nextNode] == 0:
            minret = dfs(nextNode, False)
            child += 1

            if not isRoot and minret >= nodeChecker[currentNode]:
                cut[currentNode] = 1

            ret = min(ret, minret)
        else:
            ret = min(ret, nodeChecker[nextNode])

    if isRoot and child > 1:
        cut[currentNode] = 1

    return ret


for i in range(1, V+1):
    if nodeChecker[i] == 0:
        dfs(i, True)

print(sum(cut))
for i in range(1, V+1):
    if cut[i] != 0:
        print(i, end=" ")

