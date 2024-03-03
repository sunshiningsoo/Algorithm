from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)
answers = [0 for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = [1]
isVisited = [0 for _ in range(N+1)]

while q:
    cur_node = q.pop(0)
    isVisited[cur_node] = 1
    for next_node in tree[cur_node]:
        if isVisited[next_node] == 0:
            q.append(next_node)
            isVisited[next_node] = 1
            answers[next_node] = cur_node

for i in answers[2:]:
    print(i)
