# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

answer = 0
tempMap = [[0 for _ in range(N)] for _ in range(N)]
isVisited = [0 for _ in range(N)]

for i in range(M):
    l, r = map(int, input().split())
    tempMap[l-1][r-1], tempMap[r-1][l-1] = 1, 1

def DFS(current):
    isVisited[current] = 1
    for i in range(N):
        if i != current and isVisited[i] != 1 and tempMap[current][i] == 1:
            DFS(i)


for i in range(N):
    if isVisited[i] != 1:
        DFS(i)
        answer += 1

print(answer)
