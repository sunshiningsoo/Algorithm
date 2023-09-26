N = int(input())

world = []
for i in range(N):
    world.append(list(map(int, input().split())))
whitehap = 0
bluehap = 0

def checkSum(x, y, width):
    hap = 0
    for i in range(x, x+width):
        for j in range(y, y+width):
            hap += world[i][j]
    
    return hap

def cut(x, y, width):
    temp = checkSum(x, y, width)
    if temp == 0:
        global whitehap
        whitehap += 1
        return
    if temp == width * width:
         global bluehap
         bluehap += 1
         return

    cut(x, y, width // 2)
    cut(x+width//2, y, width // 2)
    cut(x, y+width//2, width // 2)
    cut(x+width//2, y+width//2, width // 2)

cut(0, 0, N)
print(whitehap)
print(bluehap)
