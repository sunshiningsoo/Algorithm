world = [
    [0, 0, 0, 0, 4],
    [0, 2, 2, 2, 0],
    [0, 2, 0, 0, 0],
    [0, 3, 2, 0, 0],
    [3, 2, 4, 0, 0]
]

# .....
# .###.
# .#A#.
# .#.#.
# B#A#B


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
isVisited = [[0 for _ in range(len(world[0]))] for _ in range(len(world))]
target = [[], []]
for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == 3:
            target[0].append([i, j])

        if world[i][j] == 4:
            target[1].append([i, j])


def printMap():
    for i in range(len(world)):
        for j in range(len(world[0])):
            print(isVisited[i][j], end=" ")
        print()
    print()

check = False
def search(row, col, targetrow, targetcol, targetNum):
    global check
    isVisited[row][col] = 1
    if row == targetrow and col == targetcol:
        printMap()
        check = True
        return
    
    for i in range(4):
        dxx = dx[i] + row
        dyy = dy[i] + col
        if 0 <= dxx < len(world) and 0 <= dyy < len(world[0]):
            if (world[dxx][dyy] == 0 or world[dxx][dyy] == targetNum) and isVisited[dxx][dyy] == 0:
                search(dxx, dyy, targetrow, targetcol, targetNum)
                
                if not check:
                    isVisited[dxx][dyy] = 0
                else:
                    return

for i in [3, 4]:
    search(target[i-3][0][0], target[i-3][0][1], target[i-3][1][0], target[i-3][1][1], i)
    check = False

# 알파벳은 set으로 다뤄줄 수 있고, 이 set에 있는 알파벳을 이용해서 dictionary를 활용해보자! 하하

