N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

ptr = 0
str = '<'
while arr:
    ptr += K - 1
    if arr:
        ptr = ptr % len(arr)
    k = arr.pop(ptr)
    str += f'{k}, '


print(str[:-2]+">")
