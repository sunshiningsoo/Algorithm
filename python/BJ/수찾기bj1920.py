N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

_ = int(input())
check = list(map(int, input().split()))

for i in check:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == i:
            print(1)
            break
        if arr[mid] <= i:
            start = mid + 1
        else:
            end = mid - 1
    if end < start:
        print(0)
