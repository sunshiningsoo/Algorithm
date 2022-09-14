M, N = map(float, input().split())
percent = (N * 100 / M)
count = 0
start = 1
end = M

if percent >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        if (N + mid) * 100 // (M + mid) <= percent:
            start = mid + 1
        else:
            count = mid
            end = mid - 1

    print(int(count))




