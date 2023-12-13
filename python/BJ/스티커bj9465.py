n = int(input())


# 이전에 한 선택이 지금의 값에 영향을 미치는 dp 유형
def solution(cols):
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    dp = arr.copy()
    for i in range(1, len(dp[0])):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1] + arr[0][i])
        dp[1][i] = max(dp[0][i-1] + arr[1][i], dp[1][i-1])

    print(max(dp[0][-1], dp[1][-1]))


    # 지금까지 온놈의 최대값을 dp가 가지고 있자 -> 이전놈을 선택했을 경우와 선택하지 않았을 경우의 최대, 최소 값을 비교해주자


for i in range(n):
    solution(int(input()))
