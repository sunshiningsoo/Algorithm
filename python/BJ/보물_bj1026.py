N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
S.sort()
a = 0

for i in range(len(S)):
    if S[i] == 0:
        a += 1

T.sort(reverse=True)
ans = 0
for i, j in zip(S, T):
    ans += i*j

print(ans)
