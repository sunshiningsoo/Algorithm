import math

N = int(input())

arr = list(map(int, input().split()))
countOdd = 0
count = 0

for i in arr:
    countOdd = 0
    if i == 1:
        continue
    for k in range(2, i-1):
        if i%k == 0:
            countOdd += 1
    if countOdd == 0:
        count += 1


print(count)