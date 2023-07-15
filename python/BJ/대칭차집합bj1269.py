# https://www.acmicpc.net/problem/1269
_ = input()
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

k = len(list1.intersection(list2))

print(len(set(list1.union(list2))) - k)

