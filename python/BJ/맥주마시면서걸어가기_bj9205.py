from collections import deque

N = int(input())
while N:
    setter = set()
    combini = int(input())
    sx, sy = map(int, input().split())
    combis = []
    for i in range(combini):
        combis.append(list(map(int, input().split())))
    ex, ey = map(int, input().split())

    q = deque()
    q.append([sx, sy, 20])
    # 1000 보다 작은거 있으면 거기로 감 -> answer 까지 ㄱ ㄱ
    checker = False
    while q:
        cx, cy, cnt = q.popleft()
        setter.add(tuple([cx, cy]))
        if abs(cx-ex) + abs(cy-ey) <= 1000:
            checker = True
            print("happy")
            break

        for tx, ty in combis:
            if abs(tx-cx) + abs(ty-cy) <= 1000 and (tx, ty) not in setter:
                # 먼저 q에 들어가도 어짜피 이후의 코스는 똑같음
                q.append([tx, ty, 20])
                setter.add(tuple([tx, ty]))

    if not checker:
        print("sad")

    N -= 1
