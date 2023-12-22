topni = []

# N극 0, S극 1
# 1 시계방향, -1 반시계방향

# 1 시계방향, -1 반시계방향, 0 무방향

left = 6
right = 2

def printAll():
    for i in range(4):
        print(f"{topni[i][7]}  {topni[i][0]}  {topni[i][1]}", end='  ')
    print()
    for i in range(4):
        print(f"{topni[i][6]}     {topni[i][2]}", end='  ')
    print()
    for i in range(4):
        print(f"{topni[i][5]}  {topni[i][4]}  {topni[i][3]}", end='  ')
    print()


for i in range(4):
    topni.append(list(input()))

N = int(input())

for i in range(N):
    topniNum, direction = map(int, input().split())
    topniNum -= 1
    tempDir = [0] * 4
    tempDir[topniNum] = direction
    leftTopni = topniNum - 1
    rightTopni = topniNum + 1
    # printAll()
    while leftTopni >= 0:
        if topni[leftTopni][right] == topni[leftTopni+1][left]:
            tempDir[leftTopni] = 0
            break
        else:
            if tempDir[leftTopni+1] == 1:
                tempDir[leftTopni] = -1
            elif tempDir[leftTopni+1] == -1:
                tempDir[leftTopni] = 1

        leftTopni -= 1

    while rightTopni < 4:
        if topni[rightTopni][left] == topni[rightTopni-1][right]:
            tempDir[rightTopni] = 0
            break
        else:
            if tempDir[rightTopni-1] == 1:
                tempDir[rightTopni] = -1
            elif tempDir[rightTopni-1] == -1:
                tempDir[rightTopni] = 1

        rightTopni += 1
    # print(tempDir)

    for idx, value in enumerate(tempDir):
        if value == 1: # 시계
            a = topni[idx].pop()
            topni[idx].insert(0, a)
        elif value == -1: # 반시계
            a = topni[idx].pop(0)
            topni[idx].append(a)
        elif value == 0:
            continue

answer = 0
k = 1

for i in topni:
    if i[0] == '1':
        answer += k
    k *= 2

print(answer)









