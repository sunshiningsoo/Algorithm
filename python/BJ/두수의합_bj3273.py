N = int(input())
nums = list(map(int, input().split()))

nums.sort()
target = int(input())
s, e = 0, N-1
answer = 0
while s < e:
    now = nums[s] + nums[e]
    if now == target:
        answer += 1
        s += 1
    elif now > target:
        e -= 1
    else:
         s += 1
print(answer)