# https://softeer.ai/practice/info.do?idx=1&eid=624&sw_prbl_sbms_sn=227302

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

number = {
    '0': [1, 2, 3, 5, 6, 7],
    '1': [3, 6],
    '2': [1, 3, 4, 5, 7],
    '3': [1, 3, 4, 6, 7],
    '4': [2, 3, 4, 6],
    '5': [1, 2, 4, 6, 7],
    '6': [1, 2, 4, 5, 6, 7],
    '7': [1, 2, 3, 6],
    '8': [1, 2, 3, 4, 5, 6, 7],
    '9': [1, 2, 3, 4, 6, 7],
    'no': []
}

for i in range(n):
    tempFirst = []
    tempSecond = []
    for j in range(5 - len(arr[i][0])):
        tempFirst.append('no')
    for j in range(len(arr[i][0])):
        tempFirst.append(arr[i][0][j])

    for j in range(5 - len(arr[i][1])):
        tempSecond.append('no')
    for j in range(len(arr[i][1])):
        tempSecond.append(arr[i][1][j])

    # print(tempFirst)
    # print(tempSecond)

    count = 0
    for first, second in zip(tempFirst, tempSecond):
        count += len(list(set(number[first]) ^ set(number[second])))

    print(count)
    # print(len(list(set(number[arr[i][0]]) ^ (set(number[arr[i][1]])))))


