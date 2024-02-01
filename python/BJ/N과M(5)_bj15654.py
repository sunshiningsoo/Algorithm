N, target = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()



def backtrack(cur, idx):
    if len(cur) == target:
        print(*cur)
        return

    for i in range(0, len(nums)):
        if nums[i] in cur:
            continue
        backtrack(cur+[nums[i]], i)
backtrack([], 0)
