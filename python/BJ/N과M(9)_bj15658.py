N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
numSet = set()
def back(cur, idxs):
    if len(cur) == target and tuple(cur) not in numSet:
        print(*cur)
        numSet.add(tuple(cur))
        return
    if len(cur) == target:
        return

    for i in range(0, len(nums)):
        if i not in idxs:
            back(cur + [nums[i]], idxs + [i])

back([], [])
