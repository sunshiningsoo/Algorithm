target, num = map(int, input().split())
alphas = list(map(str, input().split()))
alphas.sort()
moums = ['a', 'e', 'i', 'o', 'u']
def back(cur, idx, jaum, modum):
    if len(cur) == target:
        if jaum>=2 and modum >= 1:
            print(''.join(cur))
        return
    for i in range(idx, len(alphas)):
        if alphas[i] in moums:
            back(cur + [alphas[i]], i+1, jaum, modum+1)
        else:
            back(cur + [alphas[i]], i + 1, jaum+1, modum)
back([], 0, 0, 0)
