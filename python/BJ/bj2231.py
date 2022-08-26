N = input()

# num = 0
# for i in range(int(N)):
#     if i == int(N)-1:
#         print(0)
#         break
#     num += i
#     for k in str(i):
#         num += int(k)
#
#     if num == int(N):
#         print(i)
#         break
#     else:
#         num = 0

# 안 무식한 방법
for i in range(0, int(N)):
    k = list(map(int, str(i)))
    if int(N) == sum(k)+i:
        print(i)
        break
    elif i == int(N)-1:
        print(0)