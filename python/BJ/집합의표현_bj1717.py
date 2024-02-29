import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

nodes = [i for i in range(n+1)]

def getParent(node):
    if node == nodes[node]:
        return node
    else:
        nodes[node] = getParent(nodes[node])
        return nodes[node]

def union(n1, n2):
    n1 = getParent(n1)
    n2 = getParent(n2)
    if n1 < n2:
        nodes[n2] = n1
    else:
        nodes[n1] = n2

def check(n1, n2):
    if getParent(n1) == getParent(n2):
        return True

    return False


for i in range(m):
    op, n1, n2 = map(int, input().split())
    if op == 0:
        # 합집합
        union(n1, n2)
    elif op == 1:
        # 같은 집합인지 확인
        if check(n1, n2):
            print("YES")
        else:
            print("NO")
