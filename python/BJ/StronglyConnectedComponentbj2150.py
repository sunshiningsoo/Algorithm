from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
graph = defaultdict(list)
graphTranspose = defaultdict(list)

for i in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)
    graphTranspose[e].append(s)

postorder = [0] * (V+1)
isVisited = [0] * (V+1)
num = 1


def dfs(cur):
    global num
    isVisited[cur] = 1
    for next_node in graph[cur]:
        if isVisited[next_node] == 0:
            dfs(next_node)

    postorder[cur] = num
    num += 1


for i in range(1, V+1):
    if isVisited[i] == 0:
        dfs(i)

print(postorder)
postIdx = []
for idx, value in enumerate(postorder):
    postIdx.append([idx, value])

postIdx.sort(reverse=True, key=lambda x: x[1])

isVisited = [0] * (V+1)

arr = []

def dfs2(cur, cur_arr):
    global arr
    arr = cur_arr
    isVisited[cur] = 1
    for next_node in graphTranspose[cur]:
        if isVisited[next_node] == 0:
            dfs2(next_node, arr + [next_node])

globalanswer = []
for idx, value in postIdx:
    if isVisited[idx] == 0 and idx != 0:
        arr = [idx]
        dfs2(idx, arr)
        globalanswer.append(arr)
        # print(arr)

for i in globalanswer:
    i.sort()
globalanswer.sort(key=lambda x: x[0])

print(len(globalanswer))
for i in globalanswer:
    for j in i:
        print(j, end=" ")

    print("-1")

