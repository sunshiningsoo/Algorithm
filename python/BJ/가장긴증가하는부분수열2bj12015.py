import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

answer = [-1e9]

def low_bound(num, arr):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            l = mid + 1
        elif arr[mid] > num:
            r = mid - 1

    return l


for i in arr:
    if i > answer[-1]:
        answer.append(i)
    else:
        idx = low_bound(i, answer)
        answer[idx] = i
# print(answer)
print(len(answer) - 1)
