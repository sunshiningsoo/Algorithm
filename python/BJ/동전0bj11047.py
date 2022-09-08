N, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))

count = 0
for j in arr[::-1]:
    count += K//j
    K %= j

print(count)