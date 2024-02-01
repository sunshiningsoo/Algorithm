N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
def back(cur, idx):
    if len(cur) == target:
        print(*cur)
        return
    for i in range(0, len(nums)):
        back(cur + [nums[i]], i)
back([], 0)

