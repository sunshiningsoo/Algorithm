import copy
N, M, K = map(int, input().split())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

spin = []
for i in range(K):
    spin.append(list(map(int, input().split())))

# TODO: 1. spin 순서를 만들어주고
# TODO: 2. spin 순서대로 돌리고, 각 row의 최솟값을 구하자
# TODO: 3. 전체의 최솟값 중에 global한 최솟값을 구하면 답이 나온다!

combiSpin = set()
tempWorld = copy.deepcopy(world)

def worldChange(a):
    global tempWorld
    r, c, s = a[0]-1, a[1]-1, a[2]
    realTemp = copy.deepcopy(tempWorld)

    for j in range(s): # 가장 바깥부터 안으로 돌리자
        for i in range((s-j)*2):
            # 위 아래 왼 오
            realTemp[r-s+j][c-s+i+1+j] = tempWorld[r-s+j][c-s+i+j]
            realTemp[r+s-j][c+s-i-1-j] = tempWorld[r+s-j][c+s-i-j]
            realTemp[r+s-i-1-j][c-s+j] = tempWorld[r+s-i-j][c-s+j]
            realTemp[r-s+i+1+j][c+s-j] = tempWorld[r-s+i+j][c+s-j]

    tempWorld = realTemp



minAns = []
def spins(sequence):
    global tempWorld
    tempWorld = copy.deepcopy(world)
    for idx in sequence:
        worldChange(spin[idx])

    minVal = 1e9
    for i in tempWorld:
        minVal = min(minVal, sum(i))
    minAns.append(minVal)

def combi(cur):
    if len(cur) == len(spin):
        if tuple(cur) not in combiSpin:
            combiSpin.add(tuple(cur))
        return

    for i in range(len(spin)):
        if i not in cur:
            combi(cur + [i])


for i in range(len(spin)):
    combi([i])

for i in list(combiSpin):
    spins(list(i))

print(min(minAns))
