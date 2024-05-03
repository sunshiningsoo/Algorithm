N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
l, r = 0, 1
ans = 1e9 * 10
while l < r and r < len(arr):
    cur = arr[r] - arr[l]
    if cur >= M:
        l += 1
        if l == r:
            r += 1
        ans = min(ans, cur)
    elif cur < M:
        r += 1

# while l < len(arr):
#     cur = arr[r-1] - arr[l]
#     if cur >= M:
#         ans = min(ans, cur)
#     l += 1

print(ans)
