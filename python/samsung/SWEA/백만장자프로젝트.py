from collections import deque

N = int(input())

def solution(kk):
    # 반례
    # 1
    # 10
    # 1 2 3 4 2 6 1 1 1 1
    num = int(input())
    arr = list(map(int, input().split()))
    startValue = arr.pop(0)
    arr = deque(arr)
    answer = 0
    stack = [startValue]

    while arr:
        poped = arr.popleft()
        if stack[-1] <= poped:
            stack.append(poped)
        else:
            answer = answer + stack[-1] * (len(stack) - 1) - (sum(stack) - stack[-1])
            stack = deque([poped])

    if len(stack) > 1:
        answer = answer + stack[-1] * (len(stack) - 1) - (sum(stack) - stack[-1])

    print(f"#{kk} {answer}")

def solution2(num):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    while arr:
        tempMax = max(arr)
        tempidx = arr.index(tempMax)

        answer += tempMax*tempidx - sum(arr[:tempidx])


        arr = arr[tempidx+1:]

    print(f"#{num} {answer}")



for i in range(1, N+1):
    solution2(i)
