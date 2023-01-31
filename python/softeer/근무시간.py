# https://softeer.ai/practice/info.do?idx=1&eid=990

doubleArr = []
for _ in range(5):
    doubleArr.append(input().split())

answer = 0

for i in doubleArr:
    answer += (int(i[1][:2]) - int(i[0][:2])) * 60
    if int(i[1][3:]) > int(i[0][3:]):
        answer += int(i[1][3:]) - int(i[0][3:])
    elif int(i[1][3:]) < int(i[0][3:]):
        answer += 60 - (int(i[0][3:]) - int(i[1][3:]))
        answer -= 60

print(answer)