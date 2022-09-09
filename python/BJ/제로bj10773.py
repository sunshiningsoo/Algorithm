N = int(input())

arr = [0] * N
count = 0

for k in range(N):
    temp = int(input())
    if temp == 0 and k != 0:
        count -= 1
        arr[count] = 0
    else:
        arr[count] = temp
        count += 1

print(sum(arr))