first = input()
second = input()

changeWorld = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]

for i in range(len(second)):
    changeWorld[0][i+1] = changeWorld[0][i] + 1

for i in range(len(first)):
    changeWorld[i+1][0] = changeWorld[i][0] + 1

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        if first[i-1] == second[j-1]:
            changeWorld[i][j] = min(changeWorld[i-1][j-1],
                                    changeWorld[i-1][j] + 1,
                                    changeWorld[i][j-1] + 1)
        else:
            changeWorld[i][j] = min(changeWorld[i - 1][j - 1] + 1,
                                    changeWorld[i - 1][j] + 1,
                                    changeWorld[i][j - 1] + 1)

print(changeWorld[-1][-1])
