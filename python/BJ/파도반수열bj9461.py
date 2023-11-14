N = int(input())

dp = [0] * 101
dp[0] = 1
dp[1] = 1
dp[2] = 1

def solution(n):
    if n < 3 or dp[n-1] != 0:
        return dp[n-1]
    
    for i in range(3, n):
        dp[i] = dp[i-2] + dp[i-3]
    
    return dp[n-1]


for i in range(N):
    a = int(input())
    ans = solution(a)
    print(ans)
    