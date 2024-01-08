r, c = map(int, input().split())
world = []

for i in range(r):
    world.append(list(input()))

answerWorld = [['.' for _ in range(c)] for _ in range(r)]

for i in range(c):
    stack = [] # 그냥 사과: -1, idx: 벽
    for j in range(r):
        if world[r-j-1][i] == 'a':
            stack.append(-1)
        elif world[r-j-1][i] == '#':
            stack.append(r-j-1)
    newIdx = r-1
    for idx, value in enumerate(stack):
        if value != -1:
            answerWorld[value][i] = '#'
            newIdx = value

        else:
            answerWorld[newIdx][i] = 'a'

        newIdx -= 1



for i in range(r):
    for j in range(c):
        print(answerWorld[i][j], end='')
    print()
