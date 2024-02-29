
N = int(input())
M = int(input())
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


for i in range(N):
    temp = list(map(int, input().split()))
    for idx, value in enumerate(temp):
        if idx != i:
            if value == 1:
                union(idx, i)

trab = list(map(int, input().split()))
flag = False

def check(n1, n2):
    if getParent(n1) == getParent(n2):
        return True
    return False

for i in range(1, len(trab)):
    if not check(trab[i-1]-1, trab[i]-1):
        print("NO")
        flag = True
        break

if not flag:
    print("YES")

