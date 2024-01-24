N = int(input())
nums = list(map(int, input().split()))


# 1. Stack에 집어넣음
# 2. 넣으려는 값이 Stack의 가장 마지막 요소보다 크다면,
#    가장 마지막 값보다 작을때까지 빼버리고 넣으려는 값을 넣음


stack = [[0, nums[0]]] # [idx, value]로 넣음
answer = [0] * len(nums)

for i in range(1, len(nums)):
    if stack[-1][-1] >= nums[i]:
        stack.append([i, nums[i]])
    else:
        while True:
            idx, value = stack.pop()
            answer[idx] = nums[i]
            if len(stack) == 0:
                stack.append([i, nums[i]])
                break
            if stack[-1][-1] >= nums[i]:
                stack.append([i, nums[i]])
                break

while stack:
    idx, value = stack.pop()
    answer[idx] = -1

print(*answer)
