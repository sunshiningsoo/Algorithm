sdoku = []
for i in range(9):
    sdoku.append(list(map(int, input().split())))

emptyQ = []

# 9개의 네모모양을 체크해주는 부분, row * 3 + col 하면 index가져오기 가능
squareCheck = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

# 1. 가로, 세로, 네모 에서 없는 값을 채우는 방식으로 하면 되지 않을까?
for i in range(len(sdoku)):
    for j in range(len(sdoku[0])):
        if sdoku[i][j] == 0:
            emptyQ.append([i, j])

def squareFunc(row, col):
    row = row // 3
    col = col // 3
    tempworld = [0]*9
    ans = []
    for i in range(3 * row, 3*row + 3):
        for j in range(3 * col, 3*col + 3):
            if sdoku[i][j] != 0:
                tempworld[sdoku[i][j]-1] = 1
    for idx, value in enumerate(tempworld):
        if value == 0:
            ans.append(idx+1)

    return ans

def printAll():
    for i in sdoku:
        print(*i)

def possible(row, col, j):
    for i in range(9):
        if sdoku[row][i] == j:
            return False
        if sdoku[i][col] == j:
            return False
        
    if j not in squareFunc(row, col):
        return False
        
    return True

def solution(row, col):
    rowCheck = [0] * 9
    colCheck = [0] * 9
    rowtemp = set()
    coltemp = set()

    for i in range(9):
        if sdoku[i][col] != 0:
            rowCheck[i] = 1
        if sdoku[row][i] != 0:
            colCheck[i] = 1
    for i in range(9):
        if rowCheck[i] == 0:
            rowtemp.add(i+1)
        if colCheck[i] == 0:
            coltemp.add(i+1)

    square = set(squareFunc(row, col))
    # currentDap은 가능한 답 갯수
    currentDap = rowtemp.union(coltemp.union(square))
    currentDap = list(currentDap)

    if len(emptyQ) == 0:
        sdoku[row][col] = squareFunc(row, col)[0]
        printAll()
        exit()
    for i in currentDap:
        if possible(row, col, i):
            sdoku[row][col] = i
            currentPop = emptyQ.pop(0)
            solution(currentPop[0], currentPop[1])
            emptyQ.insert(0, currentPop)
            sdoku[row][col] = 0

a = emptyQ.pop(0)
solution(a[0], a[1])