N = 5
world = [[i for i in range(N)] for _ in range(N)]

for i in world:
    print(*i)

new_world = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        new_world[i][j] = world[N-j-1][i]

print()
for i in new_world:
    print(*i)



