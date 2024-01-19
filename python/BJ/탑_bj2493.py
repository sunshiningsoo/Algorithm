import sys
input = sys.stdin.readline
N = int(input())
world = list(map(int, input().split()))
world = world[::-1]

stack = [[0, world[0]]]
answer = [0] * len(world)

for i in range(1, len(world)):
    if stack[-1][1] < world[i]:
        while stack[-1][1] < world[i]:
            idx, value = stack.pop()
            answer[len(answer) - idx - 1] = len(answer) - i
            if len(stack) == 0:
                break

    stack.append([i, world[i]])

print(*answer)

# 10
# 6 1 8 5 9 2 4 3 7 10