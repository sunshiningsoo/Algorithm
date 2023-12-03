
N, S = map(int, input().split())

arr = list(map(int, input().split()))
answer = 0
seta = []

# 현재의 값이 들어가거나 안들어가거나
checker = set()

def dfs(idx, hap, cur):
    global answer
    if hap == S and len(cur) != 0 and tuple(cur) not in checker:
        answer += 1
        checker.add(tuple(cur))
        # seta.append(cur)
    if idx >= N:
        return

    dfs(idx + 1, hap, cur)
    dfs(idx + 1, hap + arr[idx], cur + [idx])

dfs(0, 0, [])
print(answer)