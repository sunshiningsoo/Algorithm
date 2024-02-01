N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
def back(cur, idx):
    if len(cur) == target:
        print(*cur)
        return
    for i in range(idx, len(nums)):
        if nums[i] not in cur:
            back(cur + [nums[i]], i)

back([], 0)
