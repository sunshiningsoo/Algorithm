# https://softeer.ai/practice/info.do?idx=1&eid=395

W, N = map(int, input().split())
weightAndNumber = [list(map(int, input().split())) for _ in range(N)]
answer = 0
weightAndNumber.sort(key=lambda x: x[1], reverse= True)

for i in weightAndNumber:
    if i[0] >= W:
        answer += W * i[1]
        break
    else:
        answer += i[0] * i[1]
        W -= i[0]

print(answer)




