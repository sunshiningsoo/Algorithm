import sys
input = sys.stdin.readline
a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = []
l, r = 0, 0

while l != a and r != b:
    if A[l] <= B[r]:
        ans.append(A[l])
        l += 1
    else:
        ans.append(B[r])
        r += 1


if l == a:
    ans += B[r:]
elif r == b:
    ans += A[l:]
print(*ans)
