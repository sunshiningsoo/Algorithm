N, Q = map(int, input().split())
N = 2**N
world = []
for i in range(N):
    world.append(list(map(int, input().split())))
magic = list(map(int, input().split()))


def in_range(x, y):
    if 0<=x<N and 0<=y<N: return True
    return False

def total_sum():
    temp = 0
    for i in range(N):
        for j in range(N):
            if world[i][j] > 0:
                temp += world[i][j]
    return temp


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def iceSizeChecker():

    isVisited = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0

    def bfs(x, y):
        q = [[x, y]]
        cnt = 0
        isVisited[x][y] = 1
        while q:
            cr, cy = q.pop(0)
            cnt += 1
            for dx, dy in dirs:
                nx, ny = cr + dx, cy +dy
                if in_range(nx, ny) and world[nx][ny] > 0 and isVisited[nx][ny] == 0:
                    isVisited[nx][ny] = 1
                    q.append([nx, ny])
        return cnt

    for i in range(N):
        for j in range(N):
            if world[i][j] > 0 and isVisited[i][j] != 1:
                a = bfs(i, j)
                ans = max(ans, a)

    return ans


def decrease():
    t = []
    for i in range(N):
        for j in range(N):
            if world[i][j] <= 0: continue
            cnt = 0
            for dx, dy in dirs:
                nx = i + dx
                ny = j + dy
                if in_range(nx, ny) and world[nx][ny] > 0:
                    cnt += 1
            if cnt < 3:
                t.append([i, j])
    for i in t:
        world[i[0]][i[1]] -= 1


def rotate(size):
    for i in range(0, N, size):
        for j in range(0, N, size):
            # i, j 범위
            realTemp = [[0 for _ in range(size)] for _ in range(size)]

            # 잘린 네모의 가로들
            for qr in range(i, i+size):
                for qc in range(j, j+size):
                    realTemp[qc-j][size - 1 - qr+i] = world[qr][qc]

            for qr in range(size):
                for qc in range(size):
                    world[i+qr][j+qc] = realTemp[qr][qc]


for i in magic:
    rotate(2**i)
    decrease()

print(total_sum())

print(iceSizeChecker())