N = int(input())
arr = list(map(int, input().split()))

dp = [[arr[i]] for i in range(len(arr))]

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            if len(dp[i]) < len(dp[j]) + 1:
                dp[i] = dp[j] + [arr[i]]


dp.sort(key=lambda x: len(x))
print(len(dp[-1]))
print(*dp[-1])
