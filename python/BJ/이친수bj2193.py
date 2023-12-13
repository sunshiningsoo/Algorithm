n = int(input())

arr = []
for i in range(n+1):
    arr.append([0, 0])
# arr = [[0, 0]*(n+1)]
if n ==1 or n == 2:
    print(1)
    exit(0)

arr[1][1] = 1
arr[2][0] = 1
# print(arr)
if n < 3:
    print(sum(arr[n]))
    exit(0)
else:
    for i in range(3, n+1):
        arr[i] = [arr[i-1][0]+arr[i-1][1], arr[i-1][0]]

print(sum(arr[n]))
