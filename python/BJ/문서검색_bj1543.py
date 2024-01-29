originalStr = input()
target = input()

a = -1
answer = 0
for i in range(len(originalStr) - len(target)+1):
    if originalStr[i:i+len(target)] == target and a <= i:
        a = i+len(target)
        answer += 1


print(answer)

