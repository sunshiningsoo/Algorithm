N = int(input())
world = []
for i in range(N):
    world.append(list(input()))

garo = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if world[i][j] == '.':
            cnt += 1
        else:
            garo.append(cnt)
            cnt = 0
    if cnt > 0:
        garo.append(cnt)
sero = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if world[j][i] == '.':
            cnt += 1
        else:
            sero.append(cnt)
            cnt = 0
    if cnt > 0:
        sero.append(cnt)

garoC, seroC = 0, 0
for a in garo:
    if a>=2:
        garoC +=1

for a in sero:
    if a>=2:
        seroC +=1

print(garoC, seroC)

