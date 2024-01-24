munja = input()
target = input()
from collections import deque

# 처음부터 스캔하는 방식은 시간초과가 난다.
# while True:
#     curStart = []
#     for i in range(len(munja) - len(target)+1):
#         if munja[i:i+len(target)] == target:
#             curStart.append(i)
#     if len(curStart) == 0:
#         break
#     for i in curStart:
#         munja = munja[:i] + munja[i+len(target):]
#         for j in range(len(curStart)):
#             if i < curStart[j]:
#                 curStart[j] -= len(target)
#     if munja == '':
#         break
#
# if munja == '':
#     print("FRULA")
# else:
#     print(munja)


# 스택의 방식을 사용해보자

stack = []
targetLen = len(target)

for i in range(len(munja)):
    stack.append(munja[i])

    # if len(stack) >= len(target): 아래의 조건문보다 시간이 2배이상 차이남
    if stack[-1] == target[-1]:
        str = ''.join(stack[-targetLen:])
        if str == target:
            for i in range(targetLen):
                stack.pop()

if len(stack) > 0:
    print(''.join(stack))
else:
    print("FRULA")
