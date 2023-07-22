# https://www.acmicpc.net/problem/16139
import sys
input = sys.stdin.readline
target = input()
N = int(input())


# 문자열을 n번 탐색
# for i in range(N):
#     targetList = [0] * len(target)
#     alpha, start, end = map(str, input().split())
#     if target[0] == alpha:
#         targetList[0] = 1
#     for i in range(1, len(targetList)):
#         targetList[i] = targetList[i - 1]
#         if target[i] == alpha:
#             targetList[i] += 1
#
#     if start == '0':
#         print(targetList[int(end)])
#     else:
#         print(targetList[int(end)] - targetList[int(start) - 1])


# 문자열 1번 탐색으로 모든 누적합 저장!
arr = [[0 for _ in range(len(target))] for _ in range(ord('z') - ord('a')+1)]
for i in range(26):
    if target[0] == chr(i+ord('a')):
        arr[i][0] = 1
    else:
        arr[i][0] = 0
for i in range(len(target)):
    for j in range(26):
        arr[j][i] = arr[j][i-1]
        if chr(j + ord('a')) == target[i]:
            arr[j][i] += 1

for i in range(N):
    alpha, start, end = map(str, input().split())
    if start == '0':
        print(arr[ord(alpha) - ord('a')][int(end)])
    else:
        print(arr[ord(alpha) - ord('a')][int(end)] - arr[ord(alpha) - ord('a')][int(start)-1])
