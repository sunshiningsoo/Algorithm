from collections import deque
N = int(input())

arr = deque()

for i in range(N):
    arr.append(i+1)

while len(arr) != 1:
    arr.popleft()
    temp = arr.popleft()
    arr.append(temp)

print(arr.pop())
