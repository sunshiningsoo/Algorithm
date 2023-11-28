import sys
input = sys.stdin.readline
R, C = map(int, input().split())

world = []
for i in range(R):
    world.append(list(map(int, input().split())))


direct1 = [0, 1, 2, 3]
direct2 = [0, 0, 0, 0]
first = [[direct2, direct1], [direct1, direct2]]

nemo1 = [0, 0, 1, 1]
nemo2 = [0, 1, 1, 0]
second = [[nemo1, nemo2]]

change1 = [0, 1, 2, 2]
change2 = [0, 0, 0, 1]
third = [[change1, change2],
         [change2, [-1 * x for x in change1]],
         [[-1 * x for x in change1], [-1 * x for x in change2]],
         [[-1 * x for x in change2], change1]
         ]

# x, y,
# x, y-1,
# x, y-2
# x+1, y-2

# x, y,
# x, y+1,
# x, y+2,
# x-1, y+2

change1 = [0, 1, 2, 2]
change3 = [0, 0, 0, -1]
third2 = [[change1, change3],
         [change3, [-1 * x for x in change1]],
         [[-1 * x for x in change1], [-1 * x for x in change3]],
         [[-1 * x for x in change3], change1]
         ]

# x, y,
# x+1, y,
# x+2, y,
# x+2, y-1
#
# x, y,
# x, y-1,
# x, y-2,
# x-1, y-2
#
# x, y,
# x-1, y,
# x-2, y,
# x-2, y+1
#
# x, y,
# x, y+1,
# x, y+2,
# x+1, y+2

zig1 = [0, 1, 1, 2]
zig2 = [0, 0, 1, 1]
fourth = [
    [zig1, zig2],
    [zig2, [-1*x for x in zig1]],
    [[-1*x for x in zig1], [-1*x for x in zig2]],
    [zig2, zig1]
]

zig1 = [0, 1, 1, 2]
zig3 = [0, 0, -1, -1]
fourth2 = [
    [zig1, zig3],
    [zig3, [-1*x for x in zig1]],
    [[-1*x for x in zig1], [-1*x for x in zig3]],
    [zig3, zig1]
]


bolock1 = [0, 0, 0, 1]
bolock2 = [0, 1, 2, 1]
fifth = [
    [bolock1, bolock2],
    [bolock2, [-1*x for x in bolock1]],
    [[-1*x for x in bolock1], bolock2],
    [bolock2, bolock1]
]

# bolock
# x, y,
# x, y+1,
# x, y+2,
# x+1, y+1
#
# x, y,
# x+1, y,
# x+2, y,
# x+1, y-1
#
# x, y,
# x, y+1,
# x, y+2,
# x-1, y+1
#
# x, y,
# x+1, y,
# x+2, y,
# x+1, y+1


# fourth
# x, y,
# x+1, y,
# x+1, y+1,
# x+2, y+1
#
# x, y,
# x, y-1,
# x+1, y-1,
# x+1, y-2
#
# x, y,
# x-1, y,
# x-1, y-1,
# x-2, y-1
#
# x, y,
# x, y+1,
# x+1, y+1,
# x+1, y+2



# x, y,
# x+1, y,
# x+2, y,
# x+3, y,
#
#
#
# x, y,
# x, y+1,
# x, y+2

answer = []

def printOneGraph(index):
    graph = [[0 for _ in range(C)] for _ in range(R)]
    for x, y in index:
        graph[x][y] = 1

    for i in range(R):
        for j in range(C):
            print(graph[i][j], end=" ")
        print()

    print()

def solution(pattern):
    for i in range(R):
        for j in range(C):
            # 각 하나의 포인트에 대해
            for row, col in pattern:
                # 주어진 방향으로 pattern 길이만큼 돌려봄
                temp = []
                localanswer = 0
                for rr, cc in zip(row, col):
                    ii = i + rr
                    jj = j + cc
                    if 0 <= ii < R and 0 <= jj < C:
                        # print(ii, jj)
                        temp.append([ii, jj])

                if len(temp) == 4:
                    for k in temp:
                        localanswer += world[k[0]][k[1]]

                    answer.append(localanswer)


for i in [first, second, third, third2, fourth, fourth2, fifth]:
    solution(i)

print(max(answer))

# [
#     x, y,
#     x+1, y,
#     x+2, y,
#     x+2, y+1
# ]
#
# [
#     x, y,
#     x, y-1,
#     x, y-2,
#     x+1, y-2
# ]
#
# [
#     x, y,
#     x-1, y,
#     x-2, y,
#     x-2, y-1
# ]
#
# [
#     x, y,
#     x, y+1,
#     x, y+2,
#     x-1, y+2
# ]




