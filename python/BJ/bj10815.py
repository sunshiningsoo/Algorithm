a = int(input())
myList = list(map(int, input().split()))

b = int(input())
yourList = list(map(int, input().split()))

# 단순한 for 루프 서치에서는 myList를 set으로 활용하지 않는 이상, 시간초과가 뜬다.
# for i in yourList:
#     if i in myList:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")
# print("\b")


# binary search를 이용
myList.sort()

def search(i):
    start = 0
    end = a - 1
    while start <= end:
        mid = (start + end) // 2
        if myList[mid] == i:
            return 1
        elif myList[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in yourList:
    if i == yourList[-1]:
        print(search(i))
    else:
        print(search(i), end=" ")
