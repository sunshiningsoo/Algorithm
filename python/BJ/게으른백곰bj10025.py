# https://www.acmicpc.net/problem/10025
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
world = [0] * 1000001
end = 0

for i in range(N):
    a, b = map(int, input().split())
    world[b] = a
    end = max(b, end)

window = 2 * K + 1
hap = sum(world[:window])
answer = hap

for k in range(window, end+1):
    hap = hap - world[k-window] + world[k]
    answer = max(answer, hap)

print(answer)
