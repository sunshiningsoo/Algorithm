hear, watch = map(int, input().split())

hearArr = set()
watchArr = set()
for i in range(hear):
    hearArr.add(input())
for i in range(watch):
    watchArr.add(input())

new = set()
# count = 0
# for i in hearArr:
#     if i in watchArr:
#         new.add(i)
#         count += 1

# 두개의 set을 & 연산을 통해 같이 있는 데이터만 뽑아 사용이 가능해진다.
new = set(hearArr & watchArr)

print(len(new))
for i in sorted(new):
    print(i)
