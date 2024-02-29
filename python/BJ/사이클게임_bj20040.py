import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nodes = [i for i in range(N)]


def getParent(n):
    if n == nodes[n]:
        return n
    else:
        nodes[n] = getParent(nodes[n])
        return nodes[n]

def union(n1, n2):
    n1 = getParent(n1)
    n2 = getParent(n2)
    if n1 < n2:
        nodes[n2] = n1
    else:
        nodes[n1] = n2

flag = False
for i in range(M):
    n1, n2 = map(int, input().split())

    if getParent(n1) == getParent(n2):
        print(i+1)
        flag = True
        break
    else:
        union(n1, n2)

if not flag:
    print(0)