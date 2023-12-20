import sys
input = sys.stdin.readline

N, targetLength = map(int, input().split())
forest = list(map(int, input().split()))
maxNum = 1e9

l = 0
r = maxNum

def checkNum(num):
    hap = 0
    for i in forest:
        if i-num < 0:
            continue
        hap += i-num
    return hap
answer = 0

while l <= r:
    mid = (l + r) // 2
    check = checkNum(mid)

    # if check == targetLength: 딱 나눠서 떨어지는 경우가 없을 수 있음
    #     answer = mid
    #     break

    if check >= targetLength: # 나뉘어 떨어지지 않는 경우가 있을 수 있으므로, 최대로 조건을 만족하는 경우를 찾음
        answer = int(mid)
        l = mid + 1
    elif check < targetLength:
        r = mid - 1


print(answer)
