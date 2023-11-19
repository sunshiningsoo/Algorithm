N, M = map(int, input().split())

world = list(map(int, input().split()))
dpWorld = []

temp = dict()
# temp = [0] * (M)
tempHap = 0
for i in range(N):
    tempHap += world[i]
    dpWorld.append(tempHap)

    a = dpWorld[i] % M
    # temp[a] += 1
    if temp.get(a) is None:
        temp[a] = 1
    else:
        temp[a] += 1

hap = 0
if temp.get(0) is not None:
    hap = temp[0] # 길이 1개인 구간 나머지 1인 놈

for i in list(temp.keys()):
    hap += (temp[i]*(temp[i]-1) // 2)


### 요건 리스트로 구할때
# hap = temp[0]
# for i in range(M):
#     hap += (temp[i]*(temp[i]-1) // 2)

print(hap)

