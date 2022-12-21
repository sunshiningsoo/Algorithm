# REF: https://www.acmicpc.net/status?user_id=yenkee12&problem_id=1475&from_mine=1

N = input()

dic = { '0': 0, '1':0, '2': 0, '3':0, '4': 0, '5':0, '6': 0, '7':0, '8': 0, '9':0}

for i in str(N):
    if i == '6' or i == '9':
        if dic['6'] < dic['9']:
            dic['6'] += 1
        else:
            dic['9'] += 1
    else:
        dic[i] += 1

print(max(dic.values()))