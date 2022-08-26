# for문 3개 중첩
arr = []
N, M = map(int, input().split())

for i in input().split():
    arr.append(int(i))

low = 0
for i in range(0, len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            temp = arr[i]+arr[j]+arr[k]
            if low <= temp <= M:
                low = temp

print(low)

# combination 으로 3개 고르는 걸 import 해주는 방법
from itertools import combinations
low = 0
for i in combinations(arr, 3):
    if low <= sum(i) <= M:
        low = sum(i)

print(low)