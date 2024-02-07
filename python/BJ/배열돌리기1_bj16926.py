R, C, cnt = map(int, input().split())

world = []
for i in range(R):
    world.append(list(map(int, input().split())))

[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
 ]
tempR = R
tempC = C
fromout = []
for i in range(min(R, C) // 2):
    temp = []
    temp += world[0][i:len(world[0])-i+1]
    for j in range(tempR):
        temp.append(world[j])
while cnt:


    cnt -= 1