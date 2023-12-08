import sys
input = sys.stdin.readline

N = int(input())

test = list(map(int, input().split()))

B, C = map(int, input().split())

totalcount = 0

for i in test:
    temp = i

    temp -= B
    totalcount += 1
    if temp > 0:
        totalcount += temp // C
        if temp % C > 0:
            totalcount += 1
    # while temp > 0:
    #     temp -= C
    #     totalcount += 1

print(totalcount)
