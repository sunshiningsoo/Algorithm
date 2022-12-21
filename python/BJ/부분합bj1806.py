N, S = map(int, input().split())

num = list(map(int, input().split()))

start = 0
end = 1
sum = num[start]
lenCount = 100000001

while True:
    if sum < S:
        if end < len(num):
            sum += num[end]
            end += 1
        else:
            break
    elif sum >= S:
        if lenCount > end - start:
            lenCount = end - start
        sum -= num[start]
        start += 1


print(0) if lenCount == 100000001 else print(lenCount)
