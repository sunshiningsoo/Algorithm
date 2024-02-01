N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
setter = set()
def back(cur):
    if len(cur) == target and tuple(cur) not in setter:
        print(*cur)
        setter.add(tuple(cur))
        return
    if len(cur) == target:
        return
    for i in range(0, len(nums)):
        back(cur + [nums[i]])
back([])

