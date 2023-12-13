first = input()
second = input()
dp = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
# for i in dp:
#     print(*i)
