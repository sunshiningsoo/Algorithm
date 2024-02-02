def back(nums, cur, idx):
    if len(cur) == 6:
        print(*cur)
        return
    for i in range(idx, len(nums)):
        back(nums, cur + [nums[i]], i+1)

while True:
    nums = list(map(int, input().split()))
    a = nums[0]
    nums = nums[1:]
    nums.sort()
    if a == 0:
        break
    back(nums, [], 0)
    print()
