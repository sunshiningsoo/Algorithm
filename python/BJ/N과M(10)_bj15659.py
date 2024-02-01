N, target = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []


def back(cur, idx):
    if len(cur) == target and cur not in answer:
        answer.append(cur)
        print(*cur)
        return
    if len(cur) == target:
        return


    for i in range(idx, len(nums)):
        back(cur + [nums[i]], i+1)

back([], 0)


