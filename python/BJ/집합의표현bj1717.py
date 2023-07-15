# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
arr = [i for i in range(N+1)]

def unionFind(l, r):
    tl = getParent(l)
    tr = getParent(r)
    # print(tl, tr)
    if tl < tr:
        arr[tr] = tl
    else:
        arr[tl] = tr

def getParent(value):
    if value != arr[value]:
        arr[value] = getParent(arr[value])
    return arr[value]


for i in range(M):
    bit, l, r = map(int, input().split())
    if bit == 0: # union
        unionFind(l, r)
    else: # check parent
        if getParent(l) == getParent(r):
            print('YES')
        else:
            print("NO")
