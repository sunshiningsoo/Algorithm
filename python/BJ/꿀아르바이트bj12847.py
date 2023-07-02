# https://www.acmicpc.net/problem/12847
n, m = map(int, input().split())
work = list(map(int, input().split()))

hap = sum(work[:m])
answer = hap

for i in range(m, n):
    hap = hap - work[i-m] + work[i]
    answer = max(answer, hap)

print(answer)
