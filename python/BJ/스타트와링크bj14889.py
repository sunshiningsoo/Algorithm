N = int(input())

world = []
for i in range(N):
    temp = list(map(int, input().split()))
    world.append(temp)

jammy = 1000000
peopleset = []
isChecked = [0] * N

def check(isChecked):
    global jammy
    realhap = 0
    fakehap = 0
    
    for i in range(N):
        for j in range(i+1, N):
            if isChecked[i] and isChecked[j]:
                realhap += (world[i][j] + world[j][i])
            elif not isChecked[i] and not isChecked[j]:
                fakehap += (world[i][j] + world[j][i])
    
    jammy = min(jammy, abs(realhap - fakehap))


# 시간 줄이는 전략 + 순서가 필요없는 조합일 경우에 현재 depth와 추가한 index를 활용해 문제를 풀어봐라!!!
def combi(depth, index):
    if depth == N // 2:
        check(isChecked)
        return
    for i in range(index, N):
        if isChecked[i] == 0:
            isChecked[i] = 1
            combi(depth + 1, i + 1)
            isChecked[i] = 0


combi(0, 0)

print(jammy)
