N, M = map(int, input().split())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))

dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
bidirec = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
def in_range(x, y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

def move():
    global clouds, world
    direction, length = map(int, input().split())
    direction -= 1
    newPosition = set()
    for cx, cy in clouds:
        nx, ny = cx, cy
        for _ in range(length):
            nx = nx + dirs[direction][0]
            ny = ny + dirs[direction][1]

            if nx < 0:
                nx = N-1
            if ny < 0:
                ny = N-1
            if nx == N:
                nx = 0
            if ny == N:
                ny = 0

        newPosition.add((nx, ny))

    for x, y in newPosition:
        world[x][y] += 1
    for x, y in newPosition:
        cnt = 0
        for dx, dy in bidirec:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and world[nx][ny] > 0:
                cnt += 1

        world[x][y] += cnt


    clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in newPosition and world[i][j] >= 2:
               clouds.append([i, j])
               world[i][j] -= 2




for i in range(M):
    move()


ans = 0
for i in world:
    ans += sum(i)
print(ans)
