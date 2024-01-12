import sys
input = sys.stdin.readline

N = int(input())
world = []
for i in range(N):
    world.append(list(map(int, input().split())))

okpart1 = [[0, 1]] # 직선
okpart2 = [[1, 0]] # 아래로
okpart3 = [[0, 1], [1, 0], [1, 1]] # 대각선 아래로

nxdir = [[0, 1], [1, 0], [1, 1]]

obstacles = {0: okpart1, 1: okpart2, 2: okpart3}
directions = [[0, 2], [1, 2], [0, 1, 2]]
dir = 0

curx, cury = 0, 1
answer = 0

def solution(x, y, curdir):
    global answer
    if [x, y] == [N-1, N-1]:
        answer += 1
        return

    for nxtdir in directions[curdir]:
        breakable = False
        for xx, yy in obstacles[nxtdir]:
            nx = xx + x
            ny = yy + y
            if nx < N and ny < N and world[nx][ny] == 0:
                continue
            else:
                breakable = True
                break

        if not breakable:
            solution(x + nxdir[nxtdir][0], y + nxdir[nxtdir][1], nxtdir)

def solution2():
    answers = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    answers[0][0][1] = 1
    for i in range(2, N):
        if world[0][i] != 1:
            answers[0][0][i] = answers[0][0][i-1]


    for i in range(1, N):
        for j in range(2, N):
            if world[i][j] == 0 and world[i][j-1] == 0 and world[i-1][j] == 0:
                answers[2][i][j] = answers[0][i-1][j-1] + answers[1][i-1][j-1] + answers[2][i-1][j-1]
            if world[i][j] == 0:
                answers[0][i][j] = answers[0][i][j-1] + answers[2][i][j-1]
                answers[1][i][j] = answers[1][i-1][j] + answers[2][i-1][j]
    print(answers[0][-1][-1] + answers[1][-1][-1] + answers[2][-1][-1])



solution2()


# if world[-1][-1] == 1 or world[0][2] == 1:
#     print(answer)
# else:
#     solution(0, 1, 0)
#     print(answer)




