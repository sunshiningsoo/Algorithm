# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# isVisited의 사용으로 반복된 노드 탐색을 멈춰주자

def solution(maps):
    start = 0
    end = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = i
                end = j
                break

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    levor = False

    def BFS(target):
        q = [target]
        isVisited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
        while q:
            current = q.pop(0)
            y = current[0]
            x = current[1]
            isVisited[y][x] = 1
            count = current[2] + 1
            levor = current[3]

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= yy < len(maps) and 0 <= xx < len(maps[0]) and maps[yy][xx] != 'X' and isVisited[yy][xx] != 1:
                    isVisited[yy][xx] = 1
                    if maps[yy][xx] == 'E' and levor:
                        return [yy, xx, count, levor]
                    if maps[yy][xx] == 'L' and levor == False:
                        levor = True
                        return [yy, xx, count, levor]
                    q.append([yy, xx, count, levor])
        return [-1, -1, -1, -1]

    target = BFS([start, end, 0, levor])
    if target == [-1, -1, -1, -1]:
        return -1
    answerList = BFS(target)

    if answerList == [-1, -1, -1, -1]:
        return -1
    else:
        return answerList[2]
