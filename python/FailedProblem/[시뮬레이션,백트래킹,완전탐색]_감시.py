row, col = map(int, input().split())

world = []
cctvLocation = []

for i in range(row):
    world.append(list(map(int, input().split())))
    for j in range(col):
        if 0 < world[i][j] <= 5:
            cctvLocation.append([i, j, world[i][j]])

#     하  상  우  좌
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cctv = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

def emptyChecker(graph):
    counter = 0
    for i in graph:
        for j in i:
            if j == 0:
                counter += 1
    return counter

def graphCopy(graph):
    temp = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            temp[i][j] = graph[i][j]
    return temp

def printGraph(graph):
    for i in graph:
        print(*i)
    print()

def graphPaint(row_, col_, graph, directions):
    for direction in directions:
        xx = row_ + dx[direction]
        yy = col_ + dy[direction]
        while True:
            if 0<= xx < row and 0 <= yy <col:
                if graph[xx][yy] == 6:
                    break
                if graph[xx][yy] == 0:
                    graph[xx][yy] = '#'
                xx += dx[direction]
                yy += dy[direction]
            else:
                break
    # printGraph(graph)
    return graph


answerMin = 1e9

def solution(graph, dep):
    global answerMin
    if dep == len(cctvLocation):
        answerMin = min(answerMin, emptyChecker(graph))
        return
    row_, col_, cctvType = cctvLocation[dep]
    for i in cctv[cctvType]:
        temp = graphCopy(graph)
        solution(graphPaint(row_, col_, temp, i), dep + 1)

        temp = graph



solution(world, 0)
print(answerMin)
