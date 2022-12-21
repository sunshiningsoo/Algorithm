N, M = map(int, input().split())
S = []
test = []
for word in range(N):
    S.append(input())

for word in range(M):
    test.append(input())

count = 0
for word in test:
    if word in S:
        count += 1

print(count)