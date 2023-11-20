import copy

R, C = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(R)]
camera = []

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] != 0 and world[i][j] != 6:
            camera.append([world[i][j], i, j])

totalCamera = len(camera)
cameraDirection = [
    [],
    [[0], [1], [2], [3]], # 1번 카메라
    [[0, 1], [2, 3]], # 2
    [[0, 2], [0, 3], [1, 3], [1, 2]], # 3
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], # 4
    [[0, 1, 2, 3]] # 5
]
answer = 1e9

def emptyCheck(graph):
    counter = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 0:
                counter += 1
    return counter

def watch(x, y, camera_dir, graph):
    for i in camera_dir:
        nx = x
        ny = y
        while True:
            nx += direction[i][0]
            ny += direction[i][1]
            if 0<= nx < R and 0<= ny < C:
                if graph[nx][ny] == 6:
                    break
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else:
                break


def check(graph, dep):
    global answer
    if dep == totalCamera:
        answer = min(answer, emptyCheck(graph))
        return
    cameraNum, x, y = camera[dep]
    graph_copy = copy.deepcopy(graph)
    for camera_dir in cameraDirection[cameraNum]:
        watch(x, y, camera_dir, graph_copy)
        check(graph_copy, dep+1)
        graph_copy = copy.deepcopy(graph) # dfs 들어가기 전 상태


check(world, 0)
print(answer)

