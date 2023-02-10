# find sum over 300 with choosing 3 elements in arr
# REF FROM: https://leetcode.com/problems/valid-triangle-number/description/

arr = [100, 200, 100, 200, 100] # answer = 9
start, end = 0, 0
answer = 0

arr.sort()

# fix arr's first index
for i in range(0, len(arr) - 2):
    start = i + 1
    end = len(arr) - 1
    while start < end:
        if arr[i] + arr[start] + arr[end] > 300:
            answer += end - start
            end -= 1
        else:
            start += 1

# fix arr's last index
for i in range(2, len(arr)):
    start = 0
    end = i-1
    while start < end:
        if arr[start] + arr[end] + arr[i] > 300:
            answer += end - start
            end -= 1
        else:
            start += 1


print(answer)

