N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0
ans = 0
cur = arr[s]
while s <= e and e < len(arr):
    if cur == M:
        ans += 1
        cur -= arr[s]
        if s == e:
            s += 1
            e += 1
            if e == len(arr):
                break
            cur += arr[s]
        else:
            s += 1
    elif cur < M:
        e += 1
        if e == len(arr):
            break
        cur += arr[e]
    else:
        cur -= arr[s]
        if s == e:
            s += 1
            e += 1
            if e == len(arr):
                break
            cur += arr[s]
        else:
            s += 1

print(ans)

