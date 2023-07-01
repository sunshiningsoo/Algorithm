# https://www.acmicpc.net/problem/11050
N, K = input().split()
divided = 1
divider = 1

for i in range(int(K)):
    divided *= (int(N)-i)
    divider *= (i+1)

print(divided//divider)
