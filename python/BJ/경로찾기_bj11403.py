N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if world[j][i] == 1 and world[i][k] == 1:
                world[j][k] = 1



for i in world:
    print(*i)


