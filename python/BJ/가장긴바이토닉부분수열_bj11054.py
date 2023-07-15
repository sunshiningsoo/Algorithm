# https://www.acmicpc.net/problem/11054
N = int(input())
arr = list(map(int, input().split()))

dpAscending = [1] * N
dpDecending = [1] * N
reverseArr = arr[::-1].copy()

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dpAscending[i] = max(dpAscending[i], dpAscending[j] + 1)

    for j in range(i):
        if reverseArr[i] > reverseArr[j]:
            dpDecending[i] = max(dpDecending[i], dpDecending[j] + 1)

k = []
for i in range(N):
    k.append(dpAscending[i] + dpDecending[N - i - 1])

print(max(k)-1)

