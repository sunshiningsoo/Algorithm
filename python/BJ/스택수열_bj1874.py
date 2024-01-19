N = int(input())
cur = []
pointer = 1
realAnswer = []
flag =  0

for i in range(N):
    n = int(input())
    while n >= pointer:
        cur.append(pointer)
        realAnswer.append('+')
        pointer += 1

    if cur[-1] == n:
        cur.pop()
        realAnswer.append('-')
    else:
        flag = 1
        break

if flag == 1:
    print("NO")
else:
    for i in realAnswer:
        print(i)



