import copy

N = int(input())
eggs = []
for i in range(N):
    eggs.append(list(map(int, input().split())))
answer = 0


def back(idx, egg):
    global answer
    if idx == len(egg):
        temp = 0
        for i in egg:
            if i[0] <= 0:
                temp += 1
        answer = max(answer, temp)
        return

    if egg[idx][0] <= 0:
        back(idx+1, egg)
    else:
        temp = 0
        for i in range(0, len(eggs)):
            if i == idx:
                temp += 1
                continue
            if egg[i][0] <= 0:
                temp += 1
                continue

            egg[i][0] -= egg[idx][1]
            egg[idx][0] -= egg[i][1]
            back(idx+1, egg)
            egg[idx][0] += egg[i][1]
            egg[i][0] += egg[idx][1]

        if temp == N:
            back(idx+1, egg)


back(0, eggs)
print(answer)
