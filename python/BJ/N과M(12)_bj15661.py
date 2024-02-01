N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
setter = set()
def back(cur, idx):
    if len(cur) == target:
        if tuple(cur) not in setter:
            print(*cur)
            setter.add(tuple(cur))
        return

    for i in range(idx, len(nums)):
        back(cur + [nums[i]], i)

back([], 0)
